import pandas as pd
import psycopg2
from datetime import datetime

def extract():
    return pd.read_csv("data/Uncleaned_DS_jobs.csv")

def transform(df):
    return df

def load(df):
    pass

def main():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    main()
