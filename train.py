import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
import joblib

df = pd.read_csv("data/payload_full.csv")
print(df.shape)
print(df['label'].value_counts())
print(df['attack_type'].value_counts())
df['is_malicious'] = df['attack_type'].apply(lambda x: 0 if x == 'norm' else 1)
print(df['is_malicious'].value_counts())

print("Total rows:", len(df))
print("Duplicate payloads:", df['payload'].duplicated().sum())
print("Full duplicate rows:", df.duplicated().sum())

df['payload_clean'] = df['payload'].str.strip().str.lower()
print("Duplicate payloads after cleaning:", df['payload_clean'].duplicated().sum())

print("Missing payloads:", df['payload'].isna().sum())
print(df['payload'].str.len().describe())

print(df.loc[df['payload'].str.len().idxmax(), ['payload', 'attack_type']])

X_train, X_test, y_train, y_test = train_test_split(
    df['payload'],
    df['is_malicious'],
    test_size = 0.2,
    stratify = df['attack_type'],
    random_state = 42
)

print ("Train size : ", len(X_train))
print ("Test size : ", len(X_test))
print (y_train.value_counts(normalize = True))
print (y_test.value_counts(normalize = True))

print(X_train.iloc[0])
print(y_train.iloc[0])

vectorizer = TfidfVectorizer(
    analyzer='char',
    ngram_range=(1,4),
    max_features=10000
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print(X_train_vec.shape)
print(X_test_vec.shape)

model = LogisticRegression(
    max_iter=1000
)
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(y_pred)

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)
print (classification_report(y_test, y_pred))
print (confusion_matrix(y_test, y_pred))

metrics = {
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1": f1
}

joblib.dump(metrics, "models/metrics.pkl")

joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(model, "models/model.pkl")
