--CREATE TABLE students (
--
--    first_name TEXT,
--    last_name TEXT,
--    age INTEGER
--
--);
--
--CREATE TABLE employees (
--
--    first_name TEXT,
--    last_name TEXT,
--    age INTEGER
--
--);
--
--SELECT * FROM students;

--CRUD - Create, Read, Update, Delete

--INSERT INTO employees (first_name, last_name, age) VALUES ("Mike", "Stone", 25);
--
--INSERT INTO employees (first_name, last_name, age) VALUES ("Jon", "Riverwood", 23);
--
--INSERT INTO employees (first_name, last_name, age) VALUES ("Anne", "Smith", 25);
--
--INSERT INTO employees (first_name, last_name, age) VALUES ("Marry", "Anderson", 22);
--
--INSERT INTO employees (first_name, last_name, age) VALUES ("Luis", "Simons", 31);
--
--INSERT INTO employees (first_name, last_name, age) VALUES ("Tim", "Armstrong", 19);
--
--INSERT INTO employees (first_name, last_name, age) VALUES ("Jenny", "Rock", 25);
--
--INSERT INTO employees (first_name, last_name, age) VALUES ("Max", "Eastwood", 24);

SELECT * FROM employees;

SELECT first_name, last_name FROM employees WHERE first_name LIKE "J%";

--Update

UPDATE employees SET first_name="Jimm" WHERE first_name="Tim";

--Delete

DELETE FROM employees WHERE age=18;
