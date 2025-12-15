# Task 1 — Environment Setup & Tools

## Objective

Set up the complete development environment required to migrate Google Sheets–driven workflows to a PostgreSQL-compatible database using NeonDB, with scripting support and version control.

---

## Environment Overview

This task establishes a production-ready backend foundation using a managed PostgreSQL database, scripting runtime, and source control. A NeonDB free-tier cluster was used to satisfy the PostgreSQL requirement.

---

## Tools & Technologies

* **Database:** NeonDB (PostgreSQL-compatible, free-tier)
* **Runtime:** Python 3
* **Database Driver:** psycopg2
* **Environment Management:** python-dotenv
* **Version Control:** Git
* **Repository Hosting:** GitHub
* **Optional Tools:** pgAdmin / TablePlus

---

## PostgreSQL Setup

### Database Provisioning

* NeonDB account created
* Free-tier PostgreSQL cluster provisioned
* Primary branch initialized
* Database credentials generated

NeonDB was selected as it provides a fully managed PostgreSQL environment and satisfies the requirement of using PostgreSQL. Docker-based PostgreSQL was not required.

---

## Database Connection Validation

A Python script was created to verify connectivity with the PostgreSQL database using environment variables.

### Connection Test Output

```
Connected to PostgreSQL/NeonDB
```

This confirms:

* Network connectivity
* Valid credentials
* Successful PostgreSQL handshake

---

## Project Structure

```
Assignment/
├── task-1-environment
|   └──scripts
│      └── db_test.py
|   └── screenshots/
|   └── README.md
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Dependency Management

All required dependencies were installed in an isolated virtual environment and frozen into `requirements.txt` for reproducibility.

---

## Version Control

* Git repository initialized locally
* Remote GitHub repository connected
* Sensitive environment variables excluded using `.gitignore`
* Initial commit pushed to `main` branch

### Commit Reference

```
Task 1: Environment setup and NeonDB connection test
```

---

## Deliverables Completed

* NeonDB free-tier PostgreSQL cluster created
* Database credentials obtained
* PostgreSQL connection tested via Python script
* GitHub repository initialized and pushed
* Environment setup documented

---

## Task Status

**Task 1 — Completed**

The development environment is fully operational and ready for data auditing, schema design, and ETL implementation.
