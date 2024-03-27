# FastAPI MySQL CRUD API

## Note: 
Project chosen from my current database class, attached is a Jupyter notebook that shows more about the assignment specs. Huge thanks to Prof. Donald Ferguson for this amazing and practical assignment. 

This project provides a CRUD (Create, Read, Update, Delete) API built with FastAPI and MySQL, allowing you to manage students and employees. 

## Overview

Once the server is running, you can access the API using the following endpoints:

Students
- GET /students: Get all students or filter by query parameters.
- GET /students/{student_id}: Get a student by ID.
- POST /students: Create a new student.
- PUT /students/{student_id}: Update a student by ID.
- DELETE /students/{student_id}: Delete a student by ID.

Employees
- GET /employees: Get all employees or filter by query parameters.
- GET /employees/{employee_id}: Get an employee by ID.
- POST /employees: Create a new employee.
- PUT /employees/{employee_id}: Update an employee by ID.
- DELETE /employees/{employee_id}: Delete an employee by ID.


All responses are in JSON format.   