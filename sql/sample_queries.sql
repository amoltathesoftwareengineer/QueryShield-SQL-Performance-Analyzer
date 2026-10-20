
-- QueryShield: PostgreSQL Sample Queries

CREATE TABLE IF NOT EXISTS departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department_id INT REFERENCES departments(department_id),
    salary NUMERIC(10, 2),
    hire_date DATE
);

INSERT INTO departments (department_id, department_name)
VALUES
    (1, 'Engineering'),
    (2, 'Analytics'),
    (3, 'Finance')
ON CONFLICT (department_id) DO NOTHING;

INSERT INTO employees
    (employee_id, employee_name, department_id, salary, hire_date)
VALUES
    (101, 'Amit', 1, 65000, '2024-01-15'),
    (102, 'Priya', 2, 58000, '2023-08-10'),
    (103, 'Rahul', 1, 72000, '2022-05-20'),
    (104, 'Sneha', 3, 54000, '2024-03-01'),
    (105, 'Neha', 2, 61000, '2023-11-12')
ON CONFLICT (employee_id) DO NOTHING;

-- Query 1: Retrieve all employees
SELECT * FROM employees;

-- Query 2: Retrieve selected columns
SELECT employee_id, employee_name, salary
FROM employees
WHERE salary > 60000;

-- Query 3: Join employees with departments
SELECT e.employee_name, d.department_name, e.salary
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id;

-- Query 4: Aggregation by department
SELECT department_id, COUNT(*) AS employee_count,
       AVG(salary) AS average_salary
FROM employees
GROUP BY department_id;

-- Query 5: Sort employees by salary
SELECT employee_name, salary
FROM employees
ORDER BY salary DESC;

-- Query 6: Inspect the execution plan
EXPLAIN
SELECT e.employee_name, d.department_name
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id;
