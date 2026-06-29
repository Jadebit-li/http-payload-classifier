import pandas as pd
from sklearn.model_selection import train_test_split

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