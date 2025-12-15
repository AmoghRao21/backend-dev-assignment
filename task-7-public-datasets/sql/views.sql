create view avg_salary_by_title as
select job_title, avg(salary_min) as avg_min_salary
from jobs_clean
group by job_title;
