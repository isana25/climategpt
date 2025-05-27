# 🌍 ClimateGPT: Your Eco-Education Buddy

## 📘 Project Summary
**ClimateGPT** is a smart, multilingual chatbot that educates people on sustainability, climate change, carbon footprints, and green living. It uses AI-powered natural language generation and real-world data to answer relevant questions in multiple languages. The chatbot also calculates CO₂ emissions based on travel and encourages eco-friendly habits.

---

## 🛠️ Tools & Technologies Used

- **Streamlit** – Interactive web UI
- **Hugging Face Transformers** – `google/flan-t5-small` for fast, multilingual text generation
- **Climatiq API** – Real-time carbon emission calculation
- **LibreTranslate API** – Multilingual translation (English, Urdu, Spanish, French, German, Chinese)

---

## 💻 Programming Language
- Python 3.8+

---

## ✨ Features

- 🧠 **AI Chatbot**: Answers climate-related questions intelligently.
- 🌍 **Multilingual Support**: Translates replies into 6 languages including English.
- 🛣️ **Carbon Emission Estimator**: Get CO₂ emission estimates based on your travel distance.
- 🚫 **Intent Filtering**: Ignores irrelevant or off-topic queries and informs the user.
- ⚡ **Fast Responses**: Uses a lightweight model for faster answers (Flan-T5 Small).

---

## 🌐 Social Issues It Solves

1. **🌱 Climate Literacy**: Increases awareness on global warming, recycling, and green habits.
2. **💨 Carbon Awareness**: Helps individuals measure and understand their emissions.
3. **🌐 Language Inclusivity**: Makes climate knowledge accessible to non-English speakers.
4. **📲 Digital Climate Advocacy**: Easy, free, and interactive way to spread environmental consciousness.
5. **🎯 Targeted Information**: Keeps users focused on impactful, eco-relevant questions.

---

## 🚀 How to Run

1. **Clone the repository**
2. **Add Secrets** in `.streamlit/secrets.toml`:

```toml
climate_api = "your_climatiq_api_key"
