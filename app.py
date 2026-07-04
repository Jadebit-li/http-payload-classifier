import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = joblib.load("models/vectorizer.pkl")
model = joblib.load("models/model.pkl")

st.title("AI-WAF: Malicious Payload Detector")
st.markdown("A machine learning classifier that detects malicious HTTP payloads (SQLi, XSS, and more) using character-level TF-IDF and supervised learning.")
payload = st.text_input("Enter HTTP payload: ")

if st.button("Classify"):
    payload_vec =  vectorizer.transform([payload])
    prediction = model.predict(payload_vec)
    confidence = model.predict_proba(payload_vec)[0][1]

    label = "Malicious" if prediction[0] == 1 else "Benign"
    color = "#c0392b" if label == "Malicious" else "#3d9970"
    st.markdown(f"""
    <div style="background-color:{color}; padding:10px 16px; border-radius:10px; max-width: 400px">
        <h2 style="color:white; margin:0;">{label}</h2>
        <p style="color:white; margin:5px 0 0 0;">Malicious Probability: {confidence:.2%}</p>
    </div>
""", unsafe_allow_html=True)
