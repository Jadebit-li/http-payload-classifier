import streamlit as st
import joblib

vectorizer = joblib.load("models/vectorizer.pkl")
model = joblib.load("models/model.pkl")
metrics = joblib.load("models/metrics.pkl")

st.title("AI-WAF: Malicious Payload Detector")
st.markdown(
    "A machine learning classifier that detects malicious HTTP payloads "
    "(SQLi, XSS, and more) using character-level TF-IDF and supervised learning."
)

payload = st.text_input("Enter HTTP payload:")

if st.button("Classify"):

    payload_vec = vectorizer.transform([payload])

    prediction = model.predict(payload_vec)
    probs = model.predict_proba(payload_vec)[0]

    if prediction[0] == 1:
        label = "Malicious"
        confidence = probs[1]
        color = "#c0392b"
    else:
        label = "Benign"
        confidence = probs[0]
        color = "#3d9970"

    st.markdown(f"""
    <div style="background-color:{color};
                padding:10px 16px;
                border-radius:10px;
                max-width:450px;">
        <h2 style="color:white; margin:0;">{label}</h2>
        <p style="color:white; margin:5px 0 0 0;">
            Confidence: {confidence:.2%}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("### Confidence")
    st.progress(confidence)

    with st.expander("📊 Model Performance"):

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Accuracy", f"{metrics['accuracy']:.2%}")
            st.metric("Recall", f"{metrics['recall']:.2%}")

        with col2:
            st.metric("Precision", f"{metrics['precision']:.2%}")
            st.metric("F1 Score", f"{metrics['f1']:.2%}")