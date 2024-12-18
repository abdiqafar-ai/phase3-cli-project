from databases.models import session, Course, Teacher

def course_cli():
    while True:
        print("\nCourse Management:")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Back to Main Menu")

        choice = input("> ").strip()
        if choice == "1":
            add_course()
        elif choice == "2":
            view_courses()
        elif choice == "3":
            update_course()
        elif choice == "4":
            delete_course()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_course():
    name = input("Enter course name: ")

    print("\nAvailable Teachers:")
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"{teacher.id}. {teacher.name}")

    teacher_id = input("Enter teacher ID: ")
    teacher = session.query(Teacher).get(teacher_id)

    if teacher:
        course = Course(name=name, teacher_id=teacher.id)
        session.add(course)
        session.commit()
        print("Course added successfully!")
    else:
        print("Invalid teacher ID. Course not added.")

def view_courses():
    courses = session.query(Course).all()
    for course in courses:
        teacher_name = course.teacher.name if course.teacher else "No teacher assigned"
        print(f"\nID: {course.id}, Name: {course.name}, Teacher: {teacher_name}")

def update_course():
    course_id = input("Enter the course ID to update: ")
    course = session.query(Course).get(course_id)
    if course:
        course.name = input(f"Enter new course name (current: {course.name}): ") or course.name

        print("\nAvailable Teachers:")
        teachers = session.query(Teacher).all()
        for teacher in teachers:
            print(f"{teacher.id}. {teacher.name}")

        teacher_id = input("Enter new teacher ID (current: {course.teacher_id}): ")
        teacher = session.query(Teacher).get(teacher_id)
        if teacher:
            course.teacher_id = teacher.id
        else:
            print("Invalid teacher ID. Keeping the current teacher.")

        session.commit()
        print("Course updated successfully!")
    else:
        print("Course not found.")

def delete_course():
    course_id = input("Enter the course ID to delete: ")
    course = session.query(Course).get(course_id)
    if course:
        session.delete(course)
        session.commit()
        print("Course deleted successfully!")
    else:
        print("Course not found.")
