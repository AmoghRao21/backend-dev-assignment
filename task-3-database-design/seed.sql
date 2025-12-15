insert into departments (name, head) values
('Computer Science', 'Dr. Rao'),
('Electronics', 'Dr. Mehta'),
('Mechanical', 'Dr. Singh');

insert into students (full_name, email, year, department_id) values
('Rahul Sharma', 'rahul@example.com', 2, 1),
('Ananya Singh', 'ananya@example.com', 1, 2),
('Karan Verma', 'karan@example.com', 3, 3);

insert into courses (name, credits, department_id) values
('Data Structures', 4, 1),
('Databases', 3, 1),
('Circuits', 4, 2),
('Thermodynamics', 3, 3);

insert into enrollments (student_id, course_id, grade) values
(1, 1, 'A'),
(1, 2, 'B'),
(2, 3, 'A'),
(3, 4, 'B');
