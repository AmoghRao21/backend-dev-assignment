# Data Engineering Assignment — Backend Intern

This repository contains a complete, end‑to‑end backend/data‑engineering implementation covering environment setup, data auditing, database design, ETL pipelines, SQL optimization, Google App Script automation, public dataset optimization, and full technical documentation.

All tasks are **fully functional**, **demonstrable**, and aligned 1:1 with the assignment requirements.

---

## 📂 Repository Structure

```
Data-Engineering-Assignment
│
├── task-1-environment-setup
├── task-2-data-audit
├── task-3-database-design
├── task-4-etl
├── task-5-sql
├── task-6-app-script
├── task-7-public-datasets
│
├── images
├── logs
└── README.md
```

---

## ✅ Task Coverage Overview

| Task   | Description                            | Status      |
| ------ | -------------------------------------- | ----------- |
| Task 1 | Environment Setup                      | ✅ Completed |
| Task 2 | Data Audit & Assessment                | ✅ Completed |
| Task 3 | Database Design & ER Diagram           | ✅ Completed |
| Task 4 | ETL / Data Migration Pipeline          | ✅ Completed |
| Task 5 | SQL Development & Optimization         | ✅ Completed |
| Task 6 | Google App Script Automation           | ✅ Completed |
| Task 7 | Public Dataset Practice & Optimization | ✅ Completed |
| Task 8 | Documentation                          | ✅ Completed |

---

# 📊 ERD & Data Dictionary

## ER Diagram

The database schema is normalized to **3NF** and supports scalable ingestion and querying.

**Core Entities:**

* departments
* students
* courses
* enrollments

Relationships:

* Department → Students (1:N)
* Department → Courses (1:N)
* Students ↔ Courses (N:M via enrollments)

ER Diagram:

![ER Diagram](images/er-diagram.png)

## Data Dictionary (Core Tables)

### departments

| Column        | Type     | Description          |
| ------------- | -------- | -------------------- |
| department_id | INT (PK) | Unique department ID |
| name          | TEXT     | Department name      |
| head          | TEXT     | Department head      |

### students

| Column        | Type          | Description       |
| ------------- | ------------- | ----------------- |
| student_id    | INT (PK)      | Unique student ID |
| full_name     | TEXT          | Student name      |
| email         | TEXT (UNIQUE) | Student email     |
| year          | INT           | Academic year     |
| department_id | INT (FK)      | Linked department |

### courses

| Column        | Type     | Description         |
| ------------- | -------- | ------------------- |
| course_id     | INT (PK) | Course ID           |
| name          | TEXT     | Course name         |
| credits       | INT      | Credit value        |
| department_id | INT (FK) | Offering department |

### enrollments

| Column        | Type     | Description   |
| ------------- | -------- | ------------- |
| enrollment_id | INT (PK) | Enrollment ID |
| student_id    | INT (FK) | Student       |
| course_id     | INT (FK) | Course        |
| grade         | TEXT     | Grade         |

---

# 🔄 ETL Workflow Diagram & Description

## ETL Flow

```
Google Sheets / CSV
        ↓
Extract (Pandas)
        ↓
Transform
- Trim strings
- Normalize values
- Deduplicate emails
- Validate schema
        ↓
Load
- NeonDB (PostgreSQL)
```

## Key Features

* Deduplication by email
* Invalid row isolation
* Graceful failure handling
* Idempotent inserts

ETL scripts are located in:

```
/task-4-etl/etl
/task-7-public-datasets/etl
```

---

# 🧾 Logs & Validation Reports

## Validation Rules

* Email format validation
* Mandatory fields check
* Duplicate detection
* Referential integrity checks

## Logs

* ETL run logs
* Invalid row reasons
* Insert counts

Logs stored in:

```
/logs
```

Sample validations:

* Total rows ingested
* Rows rejected
* Rows inserted

---

# 🤖 App Script Automation Documentation

## Workflow

1. New row added in Google Sheet
2. App Script validates row
3. Valid → POST to FastAPI
4. FastAPI inserts into NeonDB
5. Sheet row updated with status

## Sheet Columns

| Column       | Purpose                    |
| ------------ | -------------------------- |
| Student Name | Input                      |
| Email        | Input                      |
| Year         | Input                      |
| Department   | Input                      |
| Status       | SUCCESS / FAILED / INVALID |
| Error        | Error message              |

## Architecture

Google Sheet → Apps Script → FastAPI → NeonDB

Screenshots:

![Sheet](images/sheet.png)
![App Script](images/appscript.png)
![Trigger](images/trigger.png)
![FastAPI](images/fastapi.png)

---

# 🚚 Migration Summary & Verification Reports

## Migration Summary

| Dataset            | Rows     | Inserted | Rejected |
| ------------------ | -------- | -------- | -------- |
| Synthetic Students | 250      | 151      | 99       |
| Chinook Sample     | Verified | Verified | —        |
| Jobs Dataset       | 672      | Loaded   | Cleaned  |

## Verification

* Row counts verified post‑load
* Foreign keys validated
* Query results cross‑checked

Sample verification queries:

```sql
SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM departments;
```

---

# ⚡ Performance & Optimization

## Optimizations Implemented

* Indexes on FK columns
* Aggregation views
* Stored procedures
* Materialized views (Task 7)

## Benchmarking

* EXPLAIN ANALYZE before/after indexes
* Query latency comparison
* CLI + visual benchmarks

---

# 📌 Final Notes

* All tasks are completed sequentially
* No assumptions left undocumented
* System is production‑ready
* Fully reproducible on NeonDB

---

✅ **Assignment fully completed and verified**
