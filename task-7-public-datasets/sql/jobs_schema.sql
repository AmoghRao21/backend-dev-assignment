create table if not exists jobs_clean (
    job_id serial primary key,
    job_title text not null,
    company_name text not null,
    location text,
    rating float,
    salary_min int,
    salary_max int,
    industry text,
    sector text,
    revenue text,
    founded_year int,
    ownership_type text,
    competitors text,
    created_at timestamptz default now()
);
