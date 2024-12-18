from databases.models import session, Assignment

def assignment_cli():
    while True:
        print("\nManage Assignments:")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Update Assignment")
        print("4. Delete Assignment")
        print("5. Search Assignments")
        print("6. Back to Main Menu")

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
                print(f"ID: {assignment.id}, Title: {assignment.title}, Course ID: {assignment.course_id}")

        elif choice == "3":
            assignment_id = input("Enter Assignment ID to update: ")
            assignment = session.query(Assignment).get(assignment_id)
            if assignment:
                assignment.title = input(f"Enter new title (current: {assignment.title}): ")
                session.commit()
                print("Assignment updated successfully!")
            else:
                print("Assignment not found.")

        elif choice == "4":
            assignment_id = input("Enter Assignment ID to delete: ")
            assignment = session.query(Assignment).get(assignment_id)
            if assignment:
                confirmation = input(f"Are you sure you want to delete {assignment.title}? (y/n): ").strip().lower()
                if confirmation == 'y':
                    session.delete(assignment)
                    session.commit()
                    print("Assignment deleted successfully!")
                else:
                    print("Deletion cancelled.")
            else:
                print("Assignment not found.")

        elif choice == "5":
            search_title = input("Enter assignment title to search: ").strip()
            assignments = session.query(Assignment).filter(Assignment.title.contains(search_title)).all()
            if assignments:
                for assignment in assignments:
                    print(f"ID: {assignment.id}, Title: {assignment.title}, Course ID: {assignment.course_id}")
            else:
                print("No assignments found with that title.")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")
