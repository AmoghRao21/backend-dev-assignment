import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

load_dotenv()

app = FastAPI()

class StudentPayload(BaseModel):
    full_name: str
    email: str
    year: int
    department: str

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        sslmode="require"
    )

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/register-student")
def register_student(payload: StudentPayload):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "insert into departments (name) values (%s) on conflict (name) do nothing",
        (payload.department,)
    )

    cur.execute(
        "select department_id from departments where name = %s",
        (payload.department,)
    )

    dept_id = cur.fetchone()[0]

    try:
        cur.execute(
            """
            insert into students (full_name, email, year, department_id)
            values (%s, %s, %s, %s)
            on conflict (email) do nothing
            """,
            (payload.full_name, payload.email.lower(), payload.year, dept_id)
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    finally:
        cur.close()
        conn.close()

    return {"status": "registered"}
