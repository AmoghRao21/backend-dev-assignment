# Task 2 — Data Audit & Assessment

## Overview

This task focuses on auditing raw data before migrating it into a relational database. The goal is to understand the structure, identify data quality issues, derive entities and relationships, and prepare the groundwork for schema design and ETL pipelines.

As clarified by the assignment mentor, the Google Sheets mentioned are for reference only. A **synthetic but realistic Google Sheet** was created to simulate real-world, manually maintained data with common inconsistencies.

---

## Dataset Details

* **Dataset Name:** Student Registration (Synthetic)
* **File:** `student_registration_raw.csv`
* **Rows:** 250
* **Columns:** 10
* **Source Type:** Simulated Google Sheet
* **Maintenance Style:** Manual data entry by non-technical users

The dataset intentionally contains missing values, duplicates, invalid formats, and inconsistent categorical values to reflect real production intake data.

---

## Row Semantics

**Each row represents a single student registration entry captured at the time of enrollment.**

Key implications:

* Rows are not guaranteed to be unique
* Rows may be incomplete or invalid
* No primary key exists in the raw data

---

## Column Inventory

| Column Name       | Description              |
| ----------------- | ------------------------ |
| Student Name      | Full name of the student |
| Email             | Student email address    |
| Phone             | Contact phone number     |
| DOB               | Date of birth            |
| Gender            | Gender entered by user   |
| Department        | Academic department      |
| Year              | Academic year            |
| Registration Date | Enrollment date          |
| Status            | Enrollment status        |
| Notes             | Free-text remarks        |

---

## Data Quality Issues Identified

### 1. Missing Data

* Email, Phone, DOB, and Registration Date are missing in multiple rows
* Prevents reliable identification and communication

### 2. Duplicate Records

* Same email appears in multiple rows
* Same student names appear with formatting variations

### 3. Invalid Email Formats

* Examples include malformed addresses such as `ananya@@mail.com` and `neha@gmail`
* Breaks authentication and notification workflows

### 4. Inconsistent & Invalid Dates

* Multiple date formats used (`DD/MM/YYYY`, `YYYY-MM-DD`, `DD-MM-YY`, etc.)
* Invalid dates present (e.g., `31-04-2002`, `2004/05/33`)

### 5. Inconsistent Categorical Values

**Gender:**

* `M`, `F`, `Male`, `Female`, blank

**Department:**

* `CSE`, `C.S.E`, `Computer Science`, `ME`, `Mechanical`, `EEE`, etc.

**Status:**

* `Active`, `active`, `ACTIVE`, `Inactive`

### 6. Missing Primary Key

* No Student ID present
* Email and name are unreliable as unique identifiers

---

## Identified Entities

Based on the audit, the following entities are derived:

1. **Student**
2. **Department**
3. **Registration**

---

## Entity–Attribute–Relationship (EAR)

### Student

* student_id (generated)
* full_name
* email
* phone
* dob
* gender

### Department

* department_id (generated)
* name

### Registration

* registration_id (generated)
* student_id
* department_id
* academic_year
* registration_date
* status
* notes

---

## Column Mapping (Raw → Normalized)

| Raw Column        | Target Table  | Target Column     |
| ----------------- | ------------- | ----------------- |
| Student Name      | students      | full_name         |
| Email             | students      | email             |
| Phone             | students      | phone             |
| DOB               | students      | dob               |
| Gender            | students      | gender            |
| Department        | departments   | name              |
| Year              | registrations | academic_year     |
| Registration Date | registrations | registration_date |
| Status            | registrations | status            |
| Notes             | registrations | notes             |

---

## ETL & Cleanup Considerations

The following actions are required before database insertion:

* Trim and normalize text fields
* Validate email format
* Standardize categorical values
* Normalize department names
* Parse and validate dates
* Deduplicate records (email-based)
* Generate surrogate primary keys
* Flag or reject invalid rows

---

## Assumptions

* Dataset is synthetic but representative of real-world Google Sheets
* Validation is handled downstream (ETL / backend)
* Duplicate and invalid records are expected

---

## Task 2 Checklist

* [x] Dataset selected and justified
* [x] Row meaning defined
* [x] Data quality issues identified
* [x] Entities and attributes derived
* [x] EAR table created
* [x] Column mapping documented
* [x] Cleanup and ETL strategy outlined

---

## Status

**Task 2 — COMPLETED**

This audit directly informs database schema design, ETL pipeline implementation, and automation workflows in subsequent tasks.
