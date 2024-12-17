from databases.models import session, Assignment, Course

def assignment_cli():
    while True:
        print("\nManage Assignments:")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Update Assignment")
        print("4. Delete Assignment")
        print("5. Back to Main Menu")

        choice = input("> ").strip()

        if choice == "1":
            title = input("Enter assignment title: ")
            course_id = input("Enter course ID: ")
            assignment = Assignment(title=title, course_id=course_id)
            session.add(assignment)
            session.commit()
            print("Assignment added successfully!")
        elif choice == "2":
            assignments = session.query(Assignment).all()
            for assignment in assignments:
                print(f"{assignment.id}. {assignment.title} (Course ID: {assignment.course_id})")
        elif choice == "3":
            assignment_id = input("Enter the assignment ID to update: ")
            assignment = session.query(Assignment).get(assignment_id)
            if assignment:
                assignment.title = input(f"Enter new title (current: {assignment.title}): ")
                session.commit()
                print("Assignment updated successfully!")
            else:
                print("Assignment not found.")
        elif choice == "4":
            assignment_id = input("Enter the assignment ID to delete: ")
            assignment = session.query(Assignment).get(assignment_id)
            if assignment:
                session.delete(assignment)
                session.commit()
                print("Assignment deleted successfully!")
            else:
                print("Assignment not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
