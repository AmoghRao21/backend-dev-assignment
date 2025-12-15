select count(*) as total_students from students;

select department_id, count(*) as students_count
from students
group by department_id;

select avg(year) as average_academic_year from students;

select
  s.full_name,
  c.name as course_name,
  e.grade
from enrollments e
join students s on e.student_id = s.student_id
join courses c on e.course_id = c.course_id;

select email, count(*)
from students
group by email
having count(*) > 1;

select
  d.name as department,
  count(s.student_id) as student_count
from departments d
left join students s on d.department_id = s.department_id
group by d.name;

select
  c.name as course,
  avg(
    case
      when e.grade = 'A' then 4
      when e.grade = 'B' then 3
      when e.grade = 'C' then 2
      when e.grade = 'D' then 1
    end
  ) as average_grade
from enrollments e
join courses c on e.course_id = c.course_id
group by c.name;
