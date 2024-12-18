from databases.models import session, Course

def course_cli():
    while True:
        print("\nManage Courses:")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Search Courses")
        print("6. Back to Main Menu")

        choice = input("> ").strip()

        if choice == "1":
            name = input("Enter course name: ")
            teacher_id = input("Enter teacher ID: ")
            course = Course(name=name, teacher_id=teacher_id)
            session.add(course)
            session.commit()
            print("Course added successfully!")

        elif choice == "2":
            courses = session.query(Course).all()
            for course in courses:
                print(f"ID: {course.id}, Name: {course.name}, Teacher ID: {course.teacher_id}")

        elif choice == "3":
            course_id = input("Enter Course ID to update: ")
            course = session.query(Course).get(course_id)
            if course:
                course.name = input(f"Enter new name (current: {course.name}): ")
                session.commit()
                print("Course updated successfully!")
            else:
                print("Course not found.")

        elif choice == "4":
            course_id = input("Enter Course ID to delete: ")
            course = session.query(Course).get(course_id)
            if course:
                confirmation = input(f"Are you sure you want to delete {course.name}? (y/n): ").strip().lower()
                if confirmation == 'y':
                    session.delete(course)
                    session.commit()
                    print("Course deleted successfully!")
                else:
                    print("Deletion cancelled.")
            else:
                print("Course not found.")

        elif choice == "5":
            search_name = input("Enter course name to search: ").strip()
            courses = session.query(Course).filter(Course.name.contains(search_name)).all()
            if courses:
                for course in courses:
                    print(f"ID: {course.id}, Name: {course.name}, Teacher ID: {course.teacher_id}")
            else:
                print("No courses found with that name.")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")
