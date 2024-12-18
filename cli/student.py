from databases.models import session, Student, Course

def student_cli():
    while True:
        print("\nStudent Management:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back to Main Menu")

        choice = input("> ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_student():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    student = Student(first_name=first_name, last_name=last_name, email=email)

    print("\nAvailable Courses:")
    courses = session.query(Course).all()
    for course in courses:
        print(f"{course.id}. {course.name}")

    course_ids = input("Enter course IDs separated by commas: ").split(",")
    for course_id in course_ids:
        course = session.query(Course).get(course_id.strip())
        if course:
            student.courses.append(course)

    session.add(student)
    session.commit()
    print("Student added successfully!")

def view_students():
    students = session.query(Student).all()
    for student in students:
        print(f"\nID: {student.id}, Name: {student.first_name} {student.last_name}, Email: {student.email}")
        print("Enrolled Courses: ", end="")
        print(", ".join([course.name for course in student.courses]) or "None")

def update_student():
    student_id = input("Enter the student ID to update: ")
    student = session.query(Student).get(student_id)
    if student:
        student.first_name = input(f"Enter new first name (current: {student.first_name}): ") or student.first_name
        student.last_name = input(f"Enter new last name (current: {student.last_name}): ") or student.last_name
        student.email = input(f"Enter new email (current: {student.email}): ") or student.email

        print("\nAvailable Courses:")
        courses = session.query(Course).all()
        for course in courses:
            print(f"{course.id}. {course.name}")

        course_ids = input("Enter course IDs to enroll (separated by commas): ").split(",")
        student.courses.clear()  
        for course_id in course_ids:
            course = session.query(Course).get(course_id.strip())
            if course:
                student.courses.append(course)

        session.commit()
        print("Student updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    student_id = input("Enter the student ID to delete: ")
    student = session.query(Student).get(student_id)
    if student:
        session.delete(student)
        session.commit()
        print("Student deleted successfully!")
    else:
        print("Student not found.")
