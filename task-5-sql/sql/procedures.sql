create or replace function get_students_by_department(dept text)
returns table (
  student_id int,
  full_name text,
  email text
)
as $$
begin
  return query
  select s.student_id, s.full_name, s.email
  from students s
  join departments d on s.department_id = d.department_id
  where d.name = dept;
end;
$$ language plpgsql;
