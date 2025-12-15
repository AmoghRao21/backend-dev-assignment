create index idx_jobs_location on jobs_clean(location);
create index idx_jobs_company on jobs_clean(company_name);
create index idx_jobs_salary on jobs_clean(salary_min, salary_max);
