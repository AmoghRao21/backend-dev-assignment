import os
import re
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch
from datetime import datetime

load_dotenv()

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
    conn = psycopg2.connect(
        host=os.getenv("PGHOST"),
        dbname=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        port=5432,
        sslmode="require"
    )
    cur = conn.cursor()

    insert_sql = """
        insert into jobs_clean (
            job_title, company_name, location, rating,
            salary_min, salary_max, industry, sector,
            revenue, founded_year, ownership_type, competitors
        )
        values (
            %(job_title)s, %(company_name)s, %(location)s, %(rating)s,
            %(salary_min)s, %(salary_max)s, %(industry)s, %(sector)s,
            %(revenue)s, %(founded)s, %(type_of_ownership)s, %(competitors)s
        )
    """

    records = df.to_dict(orient="records")
    execute_batch(cur, insert_sql, records, page_size=100)

    conn.commit()
    cur.close()
    conn.close()

def main():
    df = extract()
    df = transform(df)
    print("Rows after transform:", len(df))
    load(df)

if __name__ == "__main__":
    main()
