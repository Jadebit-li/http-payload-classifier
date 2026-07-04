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
    st.markdown(f"### Result: {label}")
    st.markdown(f"Confidence(malicious): {confidence:.2%}")
