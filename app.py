# app.py

import streamlit as st
from transformers import pipeline
import requests

# 🟢 Streamlit Page Configuration (must be first Streamlit command)
st.set_page_config(page_title="ClimateGPT", layout="centered")

# 🌍 App Title and Intro
st.title("🌍 ClimateGPT: Your Eco-Education Buddy")
st.markdown("""
Welcome to **ClimateGPT**, your personal assistant for learning about climate change, sustainability, and carbon footprint.
Ask a question in any supported language, and get informative answers with optional translation!
""")

# 🌐 Climate Topics for Filtering
CLIMATE_TOPICS = [
    "climate", "carbon", "recycle", "emission", "eco", "green",
    "pollution", "environment", "sustainability", "energy", "co2"
]

# ✅ Relevance Check
def is_relevant_query(query):
    return any(word in query.lower() for word in CLIMATE_TOPICS)

# 🧠 Load the lightweight model for faster response
llm = pipeline("text2text-generation", model="google/flan-t5-small")

# 🌍 Language Mapping for LibreTranslate
LANGUAGES = {
    "English": "en",
    "Urdu": "ur",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh"
}

# 📌 LibreTranslate API Endpoint
TRANSLATE_API = "https://libretranslate.de/translate"

# 🚀 Translation function
def translate_text(text, target_lang):
    try:
        if target_lang == "en":
            return text
        payload = {
            "q": text,
            "source": "en",
            "target": target_lang,
            "format": "text"
        }
        response = requests.post(TRANSLATE_API, json=payload, timeout=10)
        return response.json().get("translatedText", text)
    except Exception as e:
        return f"Translation failed: {e}"

# 🚗 Carbon Emission Estimation via Climatiq API
def get_carbon_estimate(distance_km):
    headers = {
        "Authorization": f"Bearer {st.secrets['climate_api']}"
    }
    payload = {
        "emission_factor": {"activity_id": "passenger_vehicle-vehicle_type_car-fuel_source_na-engine_size_na-vehicle_age_na"},
        "parameters": {"distance": distance_km, "distance_unit": "km"}
    }
    try:
        response = requests.post("https://beta3.api.climatiq.io/estimate", headers=headers, json=payload)
        emissions = response.json()["co2e"]
        return f"Estimated CO₂ Emission: {emissions:.2f} kg for {distance_km} km"
    except:
        return "Failed to fetch emission estimate."

# 🧾 User Inputs
user_query = st.text_input("Ask your climate-related question:")
language = st.selectbox("Choose output language:", list(LANGUAGES.keys()))

# ✈️ Optional Carbon Estimate
with st.expander("Optional: Estimate CO₂ emissions for travel"):
    distance = st.number_input("Enter travel distance in kilometers:", min_value=0.0, step=1.0)
    if distance:
        st.info(get_carbon_estimate(distance))

# 📤 Process Query
if user_query:
    if is_relevant_query(user_query):
        response = llm(user_query, max_length=200, do_sample=False)[0]['generated_text']
    else:
        response = "❗ This chatbot only answers questions related to climate, sustainability, and eco-friendly habits."

    translated_response = translate_text(response, LANGUAGES[language])
    st.markdown("---")
    st.markdown(f"**Response:** {translated_response}")
