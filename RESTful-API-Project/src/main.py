from typing import Any, Dict

# Simple starter project to test installation and environment.
# Based on https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI, Response, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
# Explicitly included uvicorn to enable starting within main program.
# Starting within main program is a simple way to enable running
# the code within the PyCharm debugger
import uvicorn

from db import DB

# Type definitions
KV = Dict[str, Any]  # Key-value pairs

app = FastAPI()

# NOTE: In a prod environment, never put this information in code!
# There are design patterns for passing confidential information to
# application.
# TODO: You may need to change the password
db = DB(
	host="localhost",
	port=3306,
	user="root",
	password="dbuserdbuser",
	database="s24_hw2",
)


@app.get("/")
async def healthcheck():
	return HTMLResponse(content="<h1>Heartbeat</h1>", status_code=status.HTTP_200_OK)


# TODO: all methods below

# --- STUDENTS ---

@app.get("/students")
async def get_students(req: Request):
	"""Gets all students that satisfy the specified query parameters.

	For instance,
		GET http://0.0.0.0:8002/students
	should return all attributes for all students.

	For instance,
		GET http://0.0.0.0:8002/students?first_name=John&last_name=Doe #there is no John Doe in the database
		GET http://0.0.0.0:8002/students?first_name=Zared&last_name=Fenelon
	should return all attributes for students whose first name is John and last name is Doe.

	You must implement a special query parameter, `fields`. You can assume
	`fields` is a comma-separated list of attribute names. For instance,
		GET http://0.0.0.0:8002/students?first_name=John&fields=first_name,email
	should return the first name and email for students whose first name is John.
	Not every request will have a `fields` parameter.

	You can assume the query parameters are valid attribute names in the student table
	(except `fields`).

	:param req: The request that optionally contains query parameters
	:returns: A list of dicts representing students. The HTTP status should be set to 200 OK.
	"""
	# Use `dict(req.query_params)` to access query parameters
	query_params = dict(req.query_params)
	attributes = list(query_params.keys())
	if "fields" in query_params.keys():
		attributes = query_params['fields'].split(",")
		filters = {k: v for k, v in query_params.items() if k != "fields"}
		response = db.select("student", attributes, filters)
		return JSONResponse(content=response, status_code=status.HTTP_200_OK)

	response = db.select("student", [], query_params)
	return JSONResponse(content=response, status_code=status.HTTP_200_OK)

@app.get("/students/{student_id}")
async def get_student(student_id: int):
	"""Gets a student by ID.

	For instance,
		GET http://0.0.0.0:8002/students/1
	should return the student with student ID 1. The returned value should
	be a dict-like object, not a list.

	If the student ID doesn't exist, the HTTP status should be set to 404 Not Found.

	:param student_id: The ID to be matched
	:returns: If the student ID exists, a dict representing the student with HTTP status set to 200 OK.
				If the student ID doesn't exist, the HTTP status should be set to 404 Not Found.
	"""
	query_result = db.select("student", [], {"student_id": student_id})

	if not query_result:
		return JSONResponse(content={"error": "Not Found"}, status_code=status.HTTP_404_NOT_FOUND)

	response = query_result[0]
	return JSONResponse(content=response, status_code=status.HTTP_200_OK)

@app.post("/students")
async def post_student(req: Request):
	"""Creates a student.

	You can assume the body of the POST request is a JSON object that represents a student.
	You can assume the request body contains only attributes found in the student table and does not
	attempt to set `student_id`.

	For instance,
		POST http://0.0.0.0:8002/students
		{
			"first_name": "John",
			"last_name": "Doe",
			...
		}

		students { "first_name": "John", "last_name": "Doe", "email":"jd@gmail.com", "enrollment_year":"2020" }
	should create a student with the attributes specified in the request body.

	If the email is not specified in the request body, the HTTP status should be set to 400 Bad Request.
	If the email already exists in the student table, the HTTP status should be set to 400 Bad Request.
	If the enrollment year is not valid, the HTTP status should be set to 400 Bad Request.

	:param req: The request, which contains a student JSON in its body
	:returns: If the request is valid, the HTTP status should be set to 201 Created.
				If the request is not valid, the HTTP status should be set to 400 Bad Request.
	"""
	# Use `await req.json()` to access the request body
	request_body = await req.json()
	if "email" not in request_body.keys():
		return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)

	select_email_if_exists = db.select("student", ["email"], {"email": request_body["email"]})
	if select_email_if_exists:
		return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)

	if "enrollment_year" not in request_body.keys():
		return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)
	elif int(request_body["enrollment_year"]) < 2016 or int(request_body["enrollment_year"]) > 2023:
		return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)

	response = db.insert("student", request_body)
	return JSONResponse(content={"success": response}, status_code=status.HTTP_201_CREATED)

@app.put("/students/{student_id}")
async def put_student(student_id: int, req: Request):
	"""Updates a student.

	You can assume the body of the PUT request is a JSON object that represents a student.
	You can assume the request body contains only attributes found in the student table and does not
	attempt to update `student_id`.

	For instance,
		PUT http://0.0.0.0:8002/students/1
		{
			"first_name": "Joe"
		}
	should update the student with student ID 1's first name to Joe.

	If the student does not exist, the HTTP status should be set to 404 Not Found.
	If the email is set to null in the request body, the HTTP status should be set to 400 Bad Request.
	If the email already exists in the student table, the HTTP status should be set to 400 Bad Request.
	If the enrollment year is not valid, the HTTP status should be set to 400 Bad Request.

	:param student_id: The ID of the student to be updated
	:param req: The request, which contains a student JSON in its body
	:returns: If the request is valid, the HTTP status should be set to 200 OK.
				If the request is not valid, the HTTP status should be set to the appropriate error code.
	"""

	# Use `await req.json()` to access the request body
	request_body = await req.json()

	select_if_student_exists = db.select("student", ["student_id"], {"student_id": student_id})

	if not select_if_student_exists:
		return JSONResponse(content={"error": "Not Found"}, status_code=status.HTTP_404_NOT_FOUND)

	if "email" in request_body:
		if request_body["email"] is None:
			return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)

		select_email_if_exists = db.select("student", ["email"], {"email": request_body["email"]})
		if select_email_if_exists:
			return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)

	if int(request_body["enrollment_year"]) < 2016 or int(request_body["enrollment_year"]) > 2023:
		return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)

	response = db.update("student", request_body, select_if_student_exists[0])
	return JSONResponse(content={"success": response}, status_code=status.HTTP_200_OK)


@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
	"""Deletes a student.

	For instance,
		DELETE http://0.0.0.0:8002/students/1
	should delete the student with student ID 1.

	If the student does not exist, the HTTP status should be set to 404 Not Found.

	:param student_id: The ID of the student to be deleted
	:returns: If the request is valid, the HTTP status should be set to 200 OK.
				If the request is not valid, the HTTP status should be set to 404 Not Found.
	"""
	select_if_student_exists = db.select("student", ["student_id"], {"student_id": student_id})
	if not select_if_student_exists:
		return JSONResponse(content={"error": "Not Found"}, status_code=status.HTTP_404_NOT_FOUND)

	response = db.delete("student", select_if_student_exists[0])
	return JSONResponse(content={"success": response}, status_code=status.HTTP_200_OK)


# --- EMPLOYEES ---

@app.get("/employees")
async def get_employees(req: Request):
	"""Gets all employees that satisfy the specified query parameters.

	For instance,
		GET http://0.0.0.0:8002/employees
	should return all attributes for all employees.

	For instance,
		GET http://0.0.0.0:8002/employees?first_name=Don&last_name=Ferguson
	should return all attributes for employees whose first name is Don and last name is Ferguson.

	You must implement a special query parameter, `fields`. You can assume
	`fields` is a comma-separated list of attribute names. For instance,
		GET http://0.0.0.0:8002/employees?first_name=Don&fields=first_name,email
	should return the first name and email for employees whose first name is Don.
	Not every request will have a `fields` parameter.

	You can assume the query parameters are valid attribute names in the employee table
	(except `fields`).

	:param req: The request that optionally contains query parameters
	:returns: A list of dicts representing employees. The HTTP status should be set to 200 OK.
	"""
	# Use `dict(req.query_params)` to access query parameters
	query_params = dict(req.query_params)
	attributes = list(query_params.keys())
	if "fields" in query_params.keys():
		attributes = query_params['fields'].split(",")
		filters = {k: v for k, v in query_params.items() if k != "fields"}
		response = db.select("employee", attributes, filters)
		return JSONResponse(content=response, status_code=status.HTTP_200_OK)

	response = db.select("employee", [], query_params)
	return JSONResponse(content=response, status_code=status.HTTP_200_OK)


@app.get("/employees/{employee_id}")
async def get_employee(employee_id: int):
	"""Gets an employee by ID.

	For instance,
		GET http://0.0.0.0:8002/employees/1
	should return the employee with employee ID 1. The returned value should
	be a dict-like object, not a list.

	If the employee ID doesn't exist, the HTTP status should be set to 404 Not Found.

	:param employee_id: The ID to be matched
	:returns: If the employee ID exists, a dict representing the employee with HTTP status set to 200 OK.
				If the employee ID doesn't exist, the HTTP status should be set to 404 Not Found.
	"""
	query_result = db.select("employee", [], {"employee_id": employee_id})

	if not query_result:
		return JSONResponse(content={"error": "Not Found"}, status_code=status.HTTP_404_NOT_FOUND)

	response = query_result[0]
	return JSONResponse(content=response, status_code=status.HTTP_200_OK)

@app.post("/employees")
async def post_employee(req: Request):
	"""Creates an employee.

	You can assume the body of the POST request is a JSON object that represents an employee.
	You can assume the request body contains only attributes found in the employee table and does not
	attempt to set `employee_id`.

	For instance,
		POST http://0.0.0.0:8002/employees
		{
			"first_name": "Don",
			"last_name": "Ferguson",
			...
		}
	should create an employee with the attributes specified in the request body.

	If the email is not specified in the request body, the HTTP status should be set to 400 Bad Request.
	If the email already exists in the employee table, the HTTP status should be set to 400 Bad Request.
	If the employee type is not valid, the HTTP status should be set to 400 Bad Request.

	:param req: The request, which contains an employee JSON in its body
	:returns: If the request is valid, the HTTP status should be set to 201 Created.
				If the request is not valid, the HTTP status should be set to 400 Bad Request.
	"""

	# Use `await req.json()` to access the request body
	request_body = await req.json()
	if "email" not in request_body.keys():
		return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)

	select_email_if_exists = db.select("employee", ["email"], {"email": request_body["email"]})
	if select_email_if_exists:
		return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)

	if "employee_type" not in request_body.keys():
		return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)
	elif not str(request_body["employee_type"]) in ['Professor', 'Lecturer', 'Staff']:
		return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)

	response = db.insert("employee", request_body)
	return JSONResponse(content={"success": response}, status_code=status.HTTP_201_CREATED)


@app.put("/employees/{employee_id}")
async def put_employee(employee_id: int, req: Request):
	"""Updates an employee.

	You can assume the body of the PUT request is a JSON object that represents an employee.
	You can assume the request body contains only attributes found in the employee table and does not
	attempt to update `employee_id`.

	For instance,
		PUT http://0.0.0.0:8002/employees/1
		{
			"first_name": "Donald"
		}
	should update the employee with employee ID 1's first name to Donald.

	If the employee does not exist, the HTTP status should be set to 404 Not Found.
	If the email is set to null in the request body, the HTTP status should be set to 400 Bad Request.
	If the email already exists in the employee table, the HTTP status should be set to 400 Bad Request.
	If the employee type is not valid, the HTTP status should be set to 400 Bad Request.

	:param employee_id: The ID of the employee to be updated
	:param req: The request, which contains an employee JSON in its body
	:returns: If the request is valid, the HTTP status should be set to 200 OK.
				If the request is not valid, the HTTP status should be set to the appropriate error code.
	"""

	# Use `await req.json()` to access the request body
	request_body = await req.json()

	select_if_employee_exists = db.select("employee", ["employee_id"], {"employee_id": employee_id})

	if not select_if_employee_exists:
		return JSONResponse(content={"error": "Not Found"}, status_code=status.HTTP_404_NOT_FOUND)

	if "email" in request_body:
		if request_body["email"] is None:
			return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)
		select_email_if_exists = db.select("employee", ["email"], {"email": request_body["email"]})
		if select_email_if_exists:
			return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)

	if not str(request_body["employee_type"]) in ['Professor', 'Lecturer', 'Staff']:
		return JSONResponse(content={"error": "Bad Request"}, status_code=status.HTTP_400_BAD_REQUEST)

	response = db.update("employee", request_body, select_if_employee_exists[0])
	return JSONResponse(content={"success": response}, status_code=status.HTTP_200_OK)

@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
	"""Deletes an employee.

	For instance,
		DELETE http://0.0.0.0:8002/employees/1
	should delete the employee with employee ID 1.

	If the employee does not exist, the HTTP status should be set to 404 Not Found.

	:param employee_id: The ID of the employee to be deleted
	:returns: If the request is valid, the HTTP status should be set to 200 OK.
				If the request is not valid, the HTTP status should be set to 404 Not Found.
	"""
	select_if_employee_exists = db.select("employee", ["employee_id"], {"employee_id": employee_id})
	if not select_if_employee_exists:
		return JSONResponse(content={"error": "Not Found"}, status_code=status.HTTP_404_NOT_FOUND)

	response = db.delete("employee", select_if_employee_exists[0])
	return JSONResponse(content={"success": response}, status_code=status.HTTP_200_OK)


if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8002)
