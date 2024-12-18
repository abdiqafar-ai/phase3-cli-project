from databases.models import session, Teacher

def teacher_cli():
    while True:
        print("\nTeacher Management:")
        print("1. Add Teacher")
        print("2. View Teachers")
        print("3. Update Teacher")
        print("4. Delete Teacher")
        print("5. Back to Main Menu")

        choice = input("> ").strip()
        if choice == "1":
            add_teacher()
        elif choice == "2":
            view_teachers()
        elif choice == "3":
            update_teacher()
        elif choice == "4":
            delete_teacher()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_teacher():
    name = input("Enter teacher name: ")
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    print("Teacher added successfully!")

def view_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"\nID: {teacher.id}, Name: {teacher.name}")

def update_teacher():
    teacher_id = input("Enter the teacher ID to update: ")
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        teacher.name = input(f"Enter new name (current: {teacher.name}): ") or teacher.name
        session.commit()
        print("Teacher updated successfully!")
    else:
        print("Teacher not found.")

def delete_teacher():
    teacher_id = input("Enter the teacher ID to delete: ")
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print("Teacher deleted successfully!")
    else:
        print("Teacher not found.")
