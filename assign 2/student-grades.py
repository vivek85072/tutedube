student_grades = {}

while True:
    print("\n1. Add/Update Student")
    print("2. Print All Grades")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        student_grades[name] = grade
        print(f"Grade updated for {name}.")
    elif choice == "2":
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
