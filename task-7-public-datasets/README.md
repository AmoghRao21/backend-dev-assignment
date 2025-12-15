# Task 7 — Public Dataset Practice & Optimizations

## Objective

Apply ETL, database design, and performance optimization techniques on **real-world public datasets** to demonstrate production-grade data engineering skills.

This task focuses on:

* Handling both clean and messy datasets
* Designing scalable ETL pipelines
* Applying database optimizations
* Measuring and validating performance improvements

---

## Datasets Used

### 1. Clean / Normalized Dataset

**Chinook Database (PostgreSQL Sample DB)**

* Well-structured, normalized schema
* Includes artists, albums, tracks, customers, invoices
* Used to demonstrate querying, joins, and optimization on a clean relational model

### 2. Messy Dataset

**Uncleaned_DS_jobs.csv**

* Real-world job listing dataset
* Contains semantic inconsistencies such as:

  * Sentinel values (`-1` instead of NULL)
  * Mixed salary formats
  * Embedded metadata in text fields
  * Inconsistent casing and formatting

This dataset was used to demonstrate realistic data auditing, transformation, and cleanup.

---

## ETL Pipeline Overview

### Extraction

* CSV ingestion using Pandas
* Batch-based processing

### Transformation

* Column normalization
* Removal of invalid sentinel values
* Salary range parsing
* Company name cleanup
* Type coercion for numeric fields

### Loading

* Batch insertion into NeonDB
* Target table: `jobs_clean`
* Incremental-safe design

---

## Database Design

### Core Tables

* `jobs_clean` — cleaned and analytics-ready job dataset
* Chinook core tables — artists, albums, tracks, invoices

### Constraints & Design Choices

* Surrogate primary keys
* Appropriate data types
* Timestamped ingestion

---

## Optimizations Implemented

* Indexes on frequently queried columns
* Analytical views for reusable queries
* Materialized views for aggregation-heavy workloads
* Stored procedures for recurring maintenance operations

---

## Performance Benchmarking

Query performance was measured **before and after optimization** using:

* `EXPLAIN ANALYZE`
* Real execution metrics from NeonDB

📊 **Detailed benchmark results:**
➡️ [Performance Benchmarks](./benchmarks/performance.md)

---

## Validation & Verification

* Row counts verified after ETL
* Data correctness validated via sampling
* Index usage confirmed through query plans
* Materialized views refreshed and queried successfully

---

## Key Outcomes

* Demonstrated handling of both clean and messy datasets
* Built reusable, modular ETL pipelines
* Achieved measurable performance improvements
* Applied production-grade database optimization strategies

---

## Status

✅ ETL pipelines implemented
✅ Data loaded and validated
✅ Indexes, views, and procedures created
✅ Benchmarks captured and documented
✅ Task 7 completed successfully
