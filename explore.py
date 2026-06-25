import pandas as pd

df = pd.read_csv("data/payload_full.csv")
# print(df.shape)
# print(df['label'].value_counts())
# print(df['attack_type'].value_counts())
# df['is_malicious'] = df['attack_type'].apply(lambda x: 0 if x == 'norm' else 1)
# print(df['is_malicious'].value_counts())

print("Total rows:", len(df))
print("Duplicate payloads:", df['payload'].duplicated().sum())
print("Full duplicate rows:", df.duplicated().sum())

df['payload_clean'] = df['payload'].str.strip().str.lower()
print("Duplicate payloads after cleaning:", df['payload_clean'].duplicated().sum())

print("Missing payloads:", df['payload'].isna().sum())
print(df['payload'].str.len().describe())

print(df.loc[df['payload'].str.len().idxmax(), ['payload', 'attack_type']])