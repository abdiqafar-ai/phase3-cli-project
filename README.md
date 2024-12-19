### Student Management System - CLI Application

## Overview

This Student Management System is a Command-Line Interface (CLI) application built using Python, SQLAlchemy ORM, and SQLite. The system is designed to help manage students, teachers, courses, and assignments, providing the functionality to add, update, view, and delete records. The system uses a relational database, allowing you to handle real-world educational data effectively.

## Features

Student Management: Add, view, update, and delete student records.

Teacher Management: Add, view, update, and delete teacher records.

Course Management: Add, view, update, and delete course records.

Assignment Management: Add, view, update, and delete assignment records.

## Technologies Used

Python: Programming language used for the application.

SQLAlchemy: ORM library used to interact with the SQLite database.

SQLite: Lightweight relational database used for storing data.

Pipenv: Dependency management tool for handling the virtual environment and packages.

VSCode: IDE used for project development and management.

## Installation

Step 2: Install Pipenv

If you haven't installed Pipenv yet, you can do so with:

```pip install pipenv```

Step 3: Install Project Dependencies

```pipenv install``

This will set up a virtual environment with all the necessary packages.

Step 4: Activate the Virtual Environment

```pipenv shell```

# Initialize the Database

After setting up the environment, you can initialize the SQLite database by running the following commands:

>>> from databases.models import Base, engine
>>> Base.metadata.create_all(engine)

This will create the necessary tables for students, teachers, courses, and assignments.

# Run the Application

To start the CLI application, run:

python app.py

This will open the main menu, allowing you to interact with the system.

## Folder Structure

/student-management-cli
    /databases
        __init__.py
        models.py
        setup.py
        initialize_db.py
    /cli
        __init__.py
        student.py
        teacher.py
        course.py
        assignment.py
        main.py
    app.py
    Pipfile
    Pipfile.lock
    README.md
    school.db
    requirements.txt

models.py - SQLAlchemy Models

Defines the database models for Student, Teacher, Course, and Assignment using SQLAlchemy.

student.py, teacher.py, course.py, assignment.py - CLI Interfaces

These files contain functions for interacting with each entity's records via a terminal interface. Users can add, view, update, and delete records for students, teachers, courses, and assignments.

app.py - Main Entry Point

The entry point of the application. It handles the main menu and provides options to manage students, teachers, courses, and assignments.

## Usage

Once the application is up and running, you can manage the data by following these steps:

Launch the App: Run the python app.py script to enter the application.

# Manage Students

Add a new student by entering the student's first name, last name, and email.

View the list of students, update their details, or delete them.

# Manage Teachers

Add, view, update, or delete teacher records.

# Manage Courses

Add new courses, view existing ones, update their details, or delete them.

# Manage Assignments

Add, view, update, or delete assignments related to specific courses.

# Example

Here is an example of how to add a student and view all students:

$ python app.py

Welcome to the Student Management System!
Choose an option:

1. Manage Students
2. Manage Teachers
3. Manage Courses
4. Manage Assignments
5. Exit

> 1

Manage Students:

1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Back to Main Menu

> 1

Enter First name: John
Enter Last name: Doe
Enter Email: johndoe@example.com

Student added successfully!

Manage Students:

1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Back to Main Menu

> 2

ID: 1, Name: John Doe, Email: johndoe@example.com

# Contributing

Contributions are welcome! To contribute, follow these steps:

Create a new branch (git add .).

Commit your changes (git commit -m "Add feature").

Push to the branch (git push).



# License

This project is licensed under the MIT License. See the LICENSE file for more details.

