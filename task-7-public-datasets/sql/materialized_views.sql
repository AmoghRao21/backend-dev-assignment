create materialized view jobs_by_location as
select location, count(*) as job_count
from jobs_clean
group by location;

create or replace procedure refresh_jobs_views()
language plpgsql
as $$
begin
    refresh materialized view jobs_by_location;
end;
$$;
