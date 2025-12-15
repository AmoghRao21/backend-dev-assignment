import re 
import pandas as pd
import psycopg2
from datetime import datetime

def extract():
    return pd.read_csv("data/Uncleaned_DS_jobs.csv")

def transform(df):
    df = df.copy()

    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
    )

    df = df[df["job_title"] != "-1"]
    df = df[df["company_name"] != "-1"]

    df["company_name"] = df["company_name"].str.split("\n").str[0].str.strip()

    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    df["founded"] = pd.to_numeric(df["founded"], errors="coerce")

    def parse_salary(val):
        if val == "-1":
            return None, None
        nums = re.findall(r"\d+", val)
        if len(nums) >= 2:
            return int(nums[0]) * 1000, int(nums[1]) * 1000
        return None, None

    salary = df["salary_estimate"].apply(parse_salary)
    df["salary_min"] = salary.apply(lambda x: x[0])
    df["salary_max"] = salary.apply(lambda x: x[1])

    return df


def load(df):
    pass

def main():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    main()
