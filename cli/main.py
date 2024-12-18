from cli.student import student_cli
from cli.teacher import teacher_cli
from cli.course import course_cli
from cli.assignment import assignment_cli

def main_menu():
    while True:
        print("\nWelcome to the Student Management System!")
        print("Choose an option:")
        print("1. Manage Students")
        print("2. Manage Teachers")
        print("3. Manage Courses")
        print("4. Manage Assignments")
        print("5. Exit")

        choice = input("> ").strip()

        if choice == "1":
            student_cli()
        elif choice == "2":
            teacher_cli()
        elif choice == "3":
            course_cli()
        elif choice == "4":
            assignment_cli()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
