create table departments (
    department_id serial primary key,
    name text not null unique,
    head text
);

create table students (
  student_id serial primary key,
  full_name text not null,
  email text not null unique,
  year int not null check (year between 1 and 5),
  department_id int not null,
  foreign key (department_id) references departments(department_id)
);

create table courses (
  course_id serial primary key,
  name text not null,
  credits int not null check (credits > 0),
  department_id int not null,
  foreign key (department_id) references departments(department_id)
);

create table enrollments (
  enrollment_id serial primary key,
  student_id int not null,
  course_id int not null,
  grade text,
  foreign key (student_id) references students(student_id),
  foreign key (course_id) references courses(course_id),
  unique (student_id, course_id)
);

create index idx_students_email on students(email);
create index idx_students_department on students(department_id);
create index idx_courses_department on courses(department_id);
create index idx_enrollments_student on enrollments(student_id);
create index idx_enrollments_course on enrollments(course_id);


