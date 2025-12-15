import os
import re
from dotenv import load_dotenv
import psycopg2
import pandas as pd

load_dotenv()

df = pd.read_csv("data/student_data.csv")

df = df.rename(columns={
    "Student Name": "full_name",
    "Email": "email",
    "Year": "year",
    "Department": "department"
})

df = df[["full_name", "email", "year", "department"]]

df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

df["email"] = df["email"].str.lower()

email_regex = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

df = df[df["email"].apply(lambda x: isinstance(x, str) and bool(email_regex.match(x)))]

df["year"] = pd.to_numeric(df["year"], errors="coerce")
df = df[df["year"].between(1, 5)]

df = df[df["department"].notna()]
df["department"] = df["department"].str.title()

df = df.drop_duplicates(subset=["email"])

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT"),
    sslmode="require"
)

cur = conn.cursor()

departments = df["department"].unique().tolist()

for dept in departments:
    cur.execute(
        "insert into departments (name) values (%s) on conflict (name) do nothing",
        (dept,)
    )

conn.commit()

cur.execute("select department_id, name from departments")
dept_map = {name: dept_id for dept_id, name in cur.fetchall()}

student_rows = [
    (
        row["full_name"],
        row["email"],
        int(row["year"]),
        dept_map[row["department"]]
    )
    for _, row in df.iterrows()
]

cur.executemany(
    """
    insert into students (full_name, email, year, department_id)
    values (%s, %s, %s, %s)
    on conflict (email) do nothing
    """,
    student_rows
)

conn.commit()

cur.close()
conn.close()

print(f"Departments processed: {len(departments)}")
print(f"Students attempted: {len(student_rows)}")
