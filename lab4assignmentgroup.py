# Lab 4: Python Practice - Group Assignment
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 10/4/2024

# Function will add student's information IS FUNCTION WILL ADD STUDENT INFORMATION.
def add_student():
    found = False
    print("\n--------------------")
    student_ID = input("Enter Student_ID: ")

    # Will check if the student ID already exists
    for p in student:
        if student_ID == p["Student_ID"]:
            found = True
            break

    # If not found, this will add a new student
    if not found:
        name = input("Enter Name: ")
        sub = input("Enter Subject: ")
        grade = input("Enter Grade: ")
        rec = {"Student_ID": student_ID, "Name": name, "Subject": sub, "Grade": grade}
        student.append(rec)
        print("--------------------")
        print("Student record added successfully!")
        print("--------------------")
    else:
        print("\n--------------------")
        print("Student-ID is already in the system.")
        print("--------------------\n")


# Function will display student's information

def display_students():
    found = False
    print("\n--------------------------------")
    for i in student:
        found = True
        print("Student_ID: ",i["Student_ID"])
        print("Name: ", i["Name"])
        print("Subject: ", i["Subject"])
        print("Grade: ", int(i["Grade"]))
        print("--------------------\n")

    if not found:
        print("\n-----------------------------------------")
        print("No Student data Found. Please Add Student")
        print("-----------------------------------------\n")


# Search function will find a student based on specific student ID number
def search_student():
    found = False
    print("\n--------------------------------")
    usi = input("Enter a Specific Student Id:")
    usi = input("Enter the student's name: ")
    for j in student:
        if usi == j["Student_ID"]:
            found = True
            print("Student_ID: ", j["Student_ID"])
            print("Name: ", j["Name"])
            print("Subject: ", j["Subject"])
            print("Grade: ", j["Grade"])
            # Grade categorization
            grade = int(j["Grade"])
            if grade >= 90:
                print('Letter Grade: A')
            elif grade >= 80:
                print('Letter Grade: B')
            elif grade >= 70:
                print('Letter Grade: C')
            elif grade >= 60:
                print('Letter Grade: D')
            else:
                print('Letter Grade: F')
            print("--------------------\n")
            break
    if not found:
        print("\n--------------------")
        print("Student Not Found")
        print("--------------------\n")

def calculate_grade_average():
    sum_of_grades = 0
    count = 0

    for record in student:
        grade = int(record["Grade"])
        sum_of_grades += grade
        count += 1
    if count > 0:
        average_grade = sum_of_grades / count
        return average_grade
    else:
        return None

#function will display highest grade
def calculate_max_grade():
    max_grade = None

    for record in student:
        grade = int(record["Grade"])
        if max_grade is None or grade > max_grade:
            max_grade = grade
    return max_grade

def calculate_min_grade():
    min_grade = None

    for record in student:
        grade = int(record["Grade"])
        if min_grade is None or grade > min_grade:
            min_grade = grade
    return min_grade

# 4 options for the user to take with student management system

student = []
print("\n-----------------------------------------------")
print("Welcome to the Student Grades Management System")
print("------------------------------------------------\n")
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Display Average Grade")
    print("5. Display Highest Grade")
    print("6. Display Lowest Grade")
    print("7. Exit")
    op = int(input("Enter Your Choice: "))
    print("--------------------\n")

    if op == 1:
        add_student()
    elif op == 2:
        display_students()
    elif op == 3:
        search_student()
    elif op == 4:
        average_grade = calculate_grade_average()
        if average_grade is not None:
            print("Average Grade: ", average_grade)
        else:
            print("No Students Found.")
    elif op == 5:
        max_grade = calculate_max_grade()
        if max_grade is not None:
            print("Max Grade: ", max_grade)
        else:
            print("No Students Found.")
    elif op == 6:
        min_grade = calculate_min_grade()
        if min_grade is not None:
            print("Min Grade: ", min_grade)
        else:
            print("No Students Found.")
    elif op == 7:
            print("Thank you, have a nice day! \n")
            break
    else:
        print("\n--------------------")
        print("Invalid input")
        print("--------------------\n")