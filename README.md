<<<<<<< HEAD
# Phase3 CLI Project
=======
# Student Management System

The **Student Management System** is a Command-Line Interface (CLI) tool designed to manage student records in a school or college setting. It allows users to perform CRUD (Create, Read, Update, Delete) operations on student data, including:

- Adding students with their details (name, roll number, and enrolled courses).
- Updating student details or grades.
- Listing students by roll number or course.
- Deleting student records.

This application is built using Python and SQLAlchemy for database management. It stores information about students, courses, and grades in a relational database.

---

## Features

### Core Functionality

1. **Add Students**:
   Add a student with a name, roll number, and enrolled courses.

2. **List Students**:
   Retrieve student details by roll number.

3. **Update Grades**:
   Update a student's grade for a specific course.

4. **Delete Students**:
   Remove student records from the database.

---

## Database Models

The application uses the following models:

- **Student**: Stores student details (name and roll number).
- **Course**: Represents courses that students can enroll in.
- **Grade**: Tracks student grades for specific courses.
- **Teacher**: (Optional) Represents teachers in the system.

---

## Technologies Used

- **Programming Language**: Python 3.x
- **Database**: SQLite (via SQLAlchemy ORM)
- **CLI Framework**: Click


---

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- Virtual environment tool (optional but recommended)

---

## Installation

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd student_management_system

Step 2: Create and Activate a Virtual Environment 
For an isolated environment:

bash
Copy code
python -m venv venv
source venv/bin/activate    
venv\\Scripts\\activate    
Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt
Step 4: Initialize the Database
Run the application to create the database tables:

bash
Copy code
python main.py
This will create a SQLite database file (student_management.db) in the root directory.

Usage
The application is a CLI tool, and commands are executed via the terminal. Below is the syntax for using the tool:

bash
Copy code
python main.py <command> [arguments]
Available Commands
Command	Description
add-student <name> <roll_number>	Adds a student to the system with a name and roll number.
list-student <roll_number>	Lists details of a student by their roll number.
update-grade <roll_number> <grade> <course_name>	Updates a student's grade for a specific course.
delete-student <roll_number>	Deletes a student by their roll number.
Examples
Add a Student:

bash
Copy code
python main.py add-student "John Doe" 101
Adds a student named "John Doe" with roll number 101.

List a Student:

bash
Copy code
python main.py list-student 101
Retrieves details of the student with roll number 101.

Update a Grade:

bash
Copy code
python main.py update-grade 101 "A+" "Math"
Updates the grade for student 101 in the "Math" course to "A+".

Delete a Student:

bash
Copy code
python main.py delete-student 101
Removes the student with roll number 101 from the database.

Project Structure
plaintext
Copy code
student_management_system/
├── models/
│   ├── __init__.py         # Model initialization
│   ├── student.py          # Student model definition
│   ├── course.py           # Course model definition
│   ├── grade.py            # Grade model definition
│   ├── teacher.py          # Teacher model definition
├── database/
│   ├── __init__.py         # Database initialization
│   └── db_setup.py         # SQLAlchemy database setup
├── cli/
│   ├── __init__.py         # CLI initialization
│   ├── commands.py         # CLI commands implementation
├── migrations/             # Optional folder for Alembic migrations
├── main.py                 # Entry point for the application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
Troubleshooting
Database Errors: If you encounter schema or database errors, delete the database file and reinitialize it:

bash
Copy code
rm student_management.db   # On Linux/Mac
del student_management.db  # On Windows
python main.py
Command Not Found: Ensure you are in the project directory and have Python installed correctly.

Future Enhancements
Extend CLI Functionality:

Add commands for managing teachers and courses.
Add advanced search capabilities.
Web Interface:

Transform the CLI into a web-based application using frameworks like Flask or Django.
Database Enhancements:

Use a production-grade database like PostgreSQL or MySQL.
Integrate Alembic for version-controlled schema migrations.
Tests:

Add unit tests for all CLI commands.
>>>>>>> 2ba855b (well written ReadMe for CLI-based student Management System with CRUD operations and SQLALCHEMY for database management)
