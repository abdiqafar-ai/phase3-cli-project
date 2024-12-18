from databases.models import session, Student

def student_cli():
    while True:
        print("\nManage Students:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Students")
        print("6. Back to Main Menu")

        choice = input("> ").strip()

        if choice == "1":
            first_name = input("Enter First name: ")
            last_name = input("Enter Last name: ")
            email = input("Enter Email: ")
            student = Student(first_name=first_name, last_name=last_name, email=email)
            session.add(student)
            session.commit()
            print("Student added successfully!")
        
        elif choice == "2":
            students = session.query(Student).all()
            for student in students:
                print(f"ID: {student.id}, Name: {student.first_name} {student.last_name}, Email: {student.email}")

        elif choice == "3":
            student_id = input("Enter Student ID to update: ")
            student = session.query(Student).get(student_id)
            if student:
                student.first_name = input(f"Enter new First name (current: {student.first_name}): ")
                student.last_name = input(f"Enter new Last name (current: {student.last_name}): ")
                student.email = input(f"Enter new Email (current: {student.email}): ")
                session.commit()
                print("Student updated successfully!")
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = input("Enter Student ID to delete: ")
            student = session.query(Student).get(student_id)
            if student:
                confirmation = input(f"Are you sure you want to delete {student.first_name} {student.last_name}? (y/n): ").strip().lower()
                if confirmation == 'y':
                    session.delete(student)
                    session.commit()
                    print("Student deleted successfully!")
                else:
                    print("Deletion cancelled.")
            else:
                print("Student not found.")

        elif choice == "5":
            search_name = input("Enter student name to search: ").strip()
            students = session.query(Student).filter(Student.first_name.contains(search_name)).all()
            if students:
                for student in students:
                    print(f"ID: {student.id}, Name: {student.first_name} {student.last_name}, Email: {student.email}")
            else:
                print("No students found with that name.")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")
