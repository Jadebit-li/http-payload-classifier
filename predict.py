import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = joblib.load("models/vectorizer.pkl")
model = joblib.load("models/model.pkl")

payload = input("Enter Payload: ")
payload_vec =  vectorizer.transform([payload])

prediction = model.predict(payload_vec)
confidence = model.predict_proba(payload_vec)[0][1]

label = "Malicious" if prediction[0] == 1 else "Benign"

print(f"Prediction: {label}")
print(f"Confidence: {confidence:.2%}")
