import streamlit as st
import requests
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="HealthAI Assistant", layout="wide")

backend = "http://localhost:8000"

# Inject custom CSS to fix input text color for dark mode
st.markdown("""
    <style>
    input, textarea, .stTextInput > div > div > input {
        color: black !important;
        background-color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<p class='main-title'>🩺 HealthAI: Intelligent Healthcare Assistant</p>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🧾 Disease Prediction", 
    "💊 Treatment Plan", 
    "📊 Health Analytics", 
    "💬 Patient Chat"
])

# ---------------------------- Disease Prediction ----------------------------
with tab1:
    st.subheader("Describe your symptoms")
    symptoms = st.text_area("Enter your symptoms", placeholder="e.g., fever, cough, headache")

    if st.button("Predict Disease", key="predict_btn"):
        if symptoms.strip():
            try:
                res = requests.post(f"{backend}/disease/predict", json={"symptoms": symptoms})
                st.success(f"🩺 Predicted Disease: **{res.json()['prediction']}**")
            except:
                st.error("🚫 Failed to connect to backend.")
        else:
            st.warning("Please enter symptoms.")

# ---------------------------- Treatment Plan ----------------------------
with tab2:
    st.subheader("Get Treatment Plan for a Condition")
    condition = st.text_input("Condition", placeholder="e.g., diabetes")

    if st.button("Generate Plan", key="plan_btn"):
        if condition.strip():
            try:
                res = requests.post(f"{backend}/treatment/plan", json={"condition": condition})
                st.info(res.json()["plan"])
            except:
                st.error("🚫 Backend error or not connected.")
        else:
            st.warning("Please enter a condition.")

# ---------------------------- Health Analytics ----------------------------
with tab3:
    st.subheader("Vitals Input")

    col1, col2, col3 = st.columns(3)
    with col1:
        heart_rate = st.text_input("Heart Rate (e.g., 72,75,78)", "72,75,78,74,76")
    with col2:
        blood_pressure = st.text_input("Blood Pressure (e.g., 120/80,122/82)", "120/80,122/82,118/79,121/81")
    with col3:
        glucose = st.text_input("Blood Glucose (e.g., 90,95,100)", "90,95,100,92")

    if st.button("Analyze Vitals", key="vitals_btn"):
        try:
            hr = list(map(int, heart_rate.split(',')))
            bp = [tuple(map(int, x.split('/'))) for x in blood_pressure.split(',')]
            gl = list(map(int, glucose.split(',')))

            systolic = [x[0] for x in bp]
            diastolic = [x[1] for x in bp]

            st.subheader("📈 Vitals Trend Charts")
            st.line_chart({"Heart Rate": hr})
            st.line_chart({"Systolic": systolic, "Diastolic": diastolic})
            st.line_chart({"Glucose": gl})
        except:
            st.error("⚠️ Please check your input formats.")

# ---------------------------- Patient Chat ----------------------------
with tab4:
    st.subheader("Chat with HealthAI")
    chat_input = st.text_input("You", placeholder="Ask a health-related question...")

    if st.button("Send", key="chat_btn"):
        if chat_input.strip():
            try:
                res = requests.post(f"{backend}/chat/message", json={"message": chat_input})
                st.markdown(f"**HealthAI:** {res.json()['reply']}")
            except:
                st.error("🚫 Could not connect to backend.")
        else:
            st.warning("Please enter your question.")
