-- CREATE TABLE books (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     title VARCHAR(100) NOT NULL,
--     author VARCHAR(100) NOT NULL,
--     genre VARCHAR(50),
--     year INT
-- );
-- CREATE TABLE students (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     student_id VARCHAR(20) NOT NULL UNIQUE
-- );



-- CREATE TABLE faculty (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     faculty_id VARCHAR(20) UNIQUE NOT NULL,
--     role VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE borrow (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     book_id INT NOT NULL,
--     student_id INT NOT NULL,
--     borrow_date DATE NOT NULL,
--     return_date DATE,
--     FOREIGN KEY (book_id) REFERENCES books(id),
--     FOREIGN KEY (student_id) REFERENCES students(id)
-- );


-- select *from books;
-- INSERT INTO faculty (name, faculty_id, role) VALUES
-- ('Dr.S.Suresh, Ph.D', 'FAC001', 'Chief Librarian'),
-- ('Mrs.P.Dhana Lakshmi', 'FAC002', 'Assistant Librarian'),
-- ('Mr.B.Govinda Rao', 'FAC003', '	Library Assistant'),
-- ('Mrs.M.Vijaya Lakshmi	', 'FAC004', 'Library Assistant'),
-- ('Mrs.T.Lakshmi Lavanya', 'FAC005', 'Lab Assistant')

-- SELECT * from faculty;

-- INSERT INTO borrow (book_id, student_id, borrow_date, return_date) VALUES
-- (14, 7, '2024-10-01', '2024-10-15'),
-- (15, 8, '2024-10-05', '2024-10-20'),
-- (16, 9, '2024-10-10', NULL),
-- (17, 10, '2024-10-12', '2024-10-25'),
-- (14, 11, '2024-10-15', NULL),
-- (15, 13, '2024-10-15', NULL);


SELECT * from borrow;

