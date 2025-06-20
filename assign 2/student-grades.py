

student_grades = {} #basic gradebook. This creates an empty dictionary to store grades.

while True: #it will Keep the program running until the user chooses to exit.
    print("\n1. Add/Update Student")
    print("2. Print All Grades")
    print("3. Exit")
    choice = input("Enter your choice: ") #Displays a menu each time. Asks the user to choose an action.

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        student_grades[name] = grade #Add a new student and grade to the dictionary.If student already exists, then their grade will be overwritten.
        print(f"Grade updated for {name}.")
    elif choice == "2":
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    elif choice == "3": 
        break #Stop the loop and end the program.
    else:
        print("Invalid choice.")
