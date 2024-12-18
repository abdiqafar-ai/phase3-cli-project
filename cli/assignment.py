from databases.models import session, Assignment, Course

def assignment_cli():
    while True:
        print("\nAssignment Management:")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Update Assignment")
        print("4. Delete Assignment")
        print("5. Back to Main Menu")

        choice = input("> ").strip()
        if choice == "1":
            add_assignment()
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            update_assignment()
        elif choice == "4":
            delete_assignment()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_assignment():
    title = input("Enter assignment title: ")

    print("\nAvailable Courses:")
    courses = session.query(Course).all()
    for course in courses:
        print(f"{course.id}. {course.name}")

    course_id = input("Enter course ID: ")
    course = session.query(Course).get(course_id)

    if course:
        assignment = Assignment(title=title, course_id=course.id)
        session.add(assignment)
        session.commit()
        print("Assignment added successfully!")
    else:
        print("Invalid course ID. Assignment not added.")

def view_assignments():
    assignments = session.query(Assignment).all()
    for assignment in assignments:
        course_name = assignment.course.name if assignment.course else "No course assigned"
        print(f"\nID: {assignment.id}, Title: {assignment.title}, Course: {course_name}")

def update_assignment():
    assignment_id = input("Enter the assignment ID to update: ")
    assignment = session.query(Assignment).get(assignment_id)
    if assignment:
        assignment.title = input(f"Enter new title (current: {assignment.title}): ") or assignment.title

        print("\nAvailable Courses:")
        courses = session.query(Course).all()
        for course in courses:
            print(f"{course.id}. {course.name}")

        course_id = input("Enter new course ID: ")
        course = session.query(Course).get(course_id)
        if course:
            assignment.course_id = course.id
        else:
            print("Invalid course ID. Keeping the current course.")

        session.commit()
        print("Assignment updated successfully!")
    else:
        print("Assignment not found.")

def delete_assignment():
    assignment_id = input("Enter the assignment ID to delete: ")
    assignment = session.query(Assignment).get(assignment_id)
    if assignment:
        session.delete(assignment)
        session.commit()
        print("Assignment deleted successfully!")
    else:
        print("Assignment not found.")
