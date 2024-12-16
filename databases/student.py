from databases.models import session, Student

def student_cli():
  while True:
    print ("\nManage Students:")
    print("1.Add Student")
    print("2.View Students ")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Back to Main Menu")

    choice = input("> ").strip()

    if choice == "1":
      first_name = input("Enter First name: ")
      last_name = input("Enter Last name: ")
      email = input("Enter Email: ")
      student = Student(first_name = first_name, last_name = last_name, email = email)
      session.add(student)
      session.commit()
      print("Student added successfully!")
    
    elif choice == "2":
      students = session.query(Student).all() 
      for student in students:
        print(f"ID: {student.id}, Name: {student.first_name} {student.last_name}, Email: {student.email}")

    elif choice == "3":
      student_id = input("Enter Student ID: ")
      student = session.query(Student).get(student_id)
      if student:
        student.first_name = input("Enter First name: ")
        student.last_name = input("Enter Last name: ")
        student.email = input("Enter Email: ")
        # student.first_name = first_name
        # student.last_name = last_name
        # student.email = email
        session.commit()
        print("Student updated successfully!")
      else:
        print("Student not found.")

    elif choice == "4":
      student_id = input("Enter the student ID to delete: ")
      student = session.query(Student).get(student_id)
      if student:
        session.delete(student)
        session.commit()
        print("Student deleted successfully!")
      else:
        print("Student not found.")

    elif choice == "5":
      break

    else:
      print("Invalid choice. Please try again.")
