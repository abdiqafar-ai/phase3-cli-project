from databases.models import session, Teacher

def teacher_cli():
    while True:
        print("\nManage Teachers:")
        print("1. Add Teacher")
        print("2. View Teachers")
        print("3. Update Teacher")
        print("4. Delete Teacher")
        print("5. Search Teachers")
        print("6. Back to Main Menu")

        choice = input("> ").strip()

        if choice == "1":
            name = input("Enter teacher name: ")
            teacher = Teacher(name=name)
            session.add(teacher)
            session.commit()
            print("Teacher added successfully!")

        elif choice == "2":
            teachers = session.query(Teacher).all()
            for teacher in teachers:
                print(f"ID: {teacher.id}, Name: {teacher.name}")

        elif choice == "3":
            teacher_id = input("Enter Teacher ID to update: ")
            teacher = session.query(Teacher).get(teacher_id)
            if teacher:
                teacher.name = input(f"Enter new name (current: {teacher.name}): ")
                session.commit()
                print("Teacher updated successfully!")
            else:
                print("Teacher not found.")

        elif choice == "4":
            teacher_id = input("Enter Teacher ID to delete: ")
            teacher = session.query(Teacher).get(teacher_id)
            if teacher:
                confirmation = input(f"Are you sure you want to delete {teacher.name}? (y/n): ").strip().lower()
                if confirmation == 'y':
                    session.delete(teacher)
                    session.commit()
                    print("Teacher deleted successfully!")
                else:
                    print("Deletion cancelled.")
            else:
                print("Teacher not found.")

        elif choice == "5":
            search_name = input("Enter teacher name to search: ").strip()
            teachers = session.query(Teacher).filter(Teacher.name.contains(search_name)).all()
            if teachers:
                for teacher in teachers:
                    print(f"ID: {teacher.id}, Name: {teacher.name}")
            else:
                print("No teachers found with that name.")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")
