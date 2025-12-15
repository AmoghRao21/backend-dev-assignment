import pandas as pd

df = pd.read_csv("data/Uncleaned_DS_jobs.csv")

print("Shape (rows, columns):")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values per column:")
print(df.isna().sum().sort_values(ascending=False))

print("\nSample rows:")
print(df.head(3))
