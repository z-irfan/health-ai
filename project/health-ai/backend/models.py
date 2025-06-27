from transformers import pipeline

# Load the FLAN-T5 model from Hugging Face cache
chat_model = pipeline("text2text-generation", model="google/flan-t5-base")

# Hardcoded fallback for known conditions
TREATMENT_DB = {
    "diabetes": "Diabetes is typically managed through lifestyle changes, including a healthy diet, regular exercise, and monitoring blood sugar levels. Medications such as Metformin or insulin therapy may be prescribed by a doctor.",
    "hypertension": "Hypertension treatment includes dietary changes (low-sodium diet), regular physical activity, stress reduction, and possibly medications like ACE inhibitors or beta blockers.",
    "asthma": "Asthma is managed with inhalers (bronchodilators or corticosteroids), avoiding triggers, and regular monitoring of breathing.",
    "covid": "For mild COVID-19 cases, rest, fluids, and paracetamol are advised. Severe cases may require antiviral drugs or hospitalization with oxygen support.",
    "anemia": "Anemia treatment often involves iron-rich foods, iron supplements, and identifying the root cause, like internal bleeding or B12 deficiency."
}

def get_model_response(prompt: str) -> str:
    prompt_lower = prompt.lower()

    # Check if symptoms match known diseases (for fallback only)
    for condition, response in TREATMENT_DB.items():
        if condition in prompt_lower:
            return f"Condition Detected: {condition.capitalize()}.\nRecommended Treatment: {response}"

    # Reformat prompt for actual model prediction
    formatted_prompt = (
        f"A patient presents with the following symptoms: {prompt}. "
        f"What is the most likely diagnosis?"
    )

    try:
        res = chat_model(formatted_prompt, max_new_tokens=100, do_sample=False)
        return res[0]["generated_text"]
    except Exception as e:
        return f"⚠️ Model error: {str(e)}"
