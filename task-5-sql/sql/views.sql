create or replace view students_per_department as
select
  d.name as department,
  count(s.student_id) as student_count
from departments d
left join students s on d.department_id = s.department_id
group by d.name;
