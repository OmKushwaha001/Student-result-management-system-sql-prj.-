CREATE DATABASE student_result_d;

USE student_result_d;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    roll_no VARCHAR(20) NOT NULL UNIQUE,
    class VARCHAR(20) NOT NULL,
    marks INT NOT NULL
);

INSERT INTO students (name, roll_no, class, marks) VALUES
('Amit Sharma', 'R001', '10A', 85),
('Priya Verma', 'R002', '10A', 92),
('Rohit Kumar', 'R003', '10B', 78),
('Sneha Gupta', 'R004', '10B', 67),
('Vikram Singh', 'R005', '10A', 88),
('Anjali Mehta', 'R006', '10C', 95),
('Ravi Kumar', 'R007', '10A', 73);

SELECT * FROM students;


SELECT * FROM students WHERE marks > 80;


SELECT * FROM students WHERE class = '10A';


