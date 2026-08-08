import time

students = {}

# ================================= ADD STUDENT FUNCTION =================================
def add_student():

    while True:
        student_id = input("Enter student ID(e.g. K01): ").upper()
        if not student_id.isalnum():
            print("Please enter a valid ID.\n")
        elif student_id in students:
            print("ID already exists.\n")     
        else:
            break 

    while True:
        student_name = input("Enter student name: ").title()
        if not student_name.replace(" ", "").isalpha():
            print("Please enter a valid name.\n")     
        else:
            break 

    while True:
        phone = input ("Enter phone no (11 digits only , without space or hyphen): ")
        if not phone.isdigit() or len(phone)!=11:
            print("Please enter a valid phone number.\n")
        elif any(student["Phone"] == phone for student in students.values()):
            print("Phone no: already exists.\n")    
        else:
            break   

    while True:
        email = input ("Enter your university email address (e.g. abc@nu.edu.pk): ")
        if "@nu" not in email or ".edu.pk" not in email:
            print("Please enter a valid email.\n")
        elif any(student["Email"] == email for student in students.values()):
            print("Email already exists.\n")     
        else:
            break  
                

    students[student_id] ={ 
            "Name"   : student_name,
            "Phone"  : phone,
            "Email"  : email,
            "Marks"  : {}
            }
        
    print("Student added successfully!\n")                  
 
# ================================= ADD MARKS FUNCTION ===================================
def add_marks():

    student_id = input("Enter student ID to add their marks: ").upper()
    if student_id not in students:
        print("Student ID not found!")
        return

    print(f"\nStudent ID: {student_id}")        
    while True:
        OOP_marks = float(input("Enter you OOP marks (0-100): "))
        if OOP_marks < 0 or OOP_marks > 100:
            print("Marks out of range! please enter (0-100)\n")
        else:
            students[student_id]["Marks"]["OOP"] = OOP_marks
            break
    while True:        
        DLD_marks = float(input("Enter you DLD marks (0-100): "))
        if DLD_marks < 0 or DLD_marks > 100:
            print("Marks out of range! please enter (0-100)\n")
        else:
            students[student_id]["Marks"]["DLD"] = DLD_marks
            break            
    while True:
        MVC_marks = float(input("Enter you MVC marks (0-100): "))
        if MVC_marks < 0 or MVC_marks > 100:
            print("Marks out of range! please enter (0-100)\n")
        else:
            students[student_id]["Marks"]["MVC"] = MVC_marks
            break
    while True:
        CCE_marks = float(input("Enter you CCE marks (0-100): "))
        if CCE_marks < 0 or CCE_marks > 100:
            print("Marks out of range! please enter (0-100)\n")
        else:
            students[student_id]["Marks"]["CCE"] = CCE_marks 
            break            
    while True:
        PST_marks = float(input("Enter you PST marks (0-100): "))
        if PST_marks < 0 or PST_marks > 100:
            print("Marks out of range! please enter (0-100)\n")
        else:
            students[student_id]["Marks"]["PST"] = PST_marks 
            break   
        
    print("Marks added successfully!\n")     
 
# ================================= VIEW STUDENT FUNCTION ================================
def view_students():
    if not students:
        print("No student found!")
        return
    print("\n----------- Student list -----------\n")
    for id, student in students.items():
        print(f"\nStudent ID = {id}\n")

        for key, value in student.items():
            print(f"{key} : {value}") 

# ================================ CALCULATE AVG FUNCTION ================================
def calculate_average():
    student_id = input("Enter student ID to find average: ").upper()
    if student_id not in students:
        print("Student ID not found!")
        return

    marks = students[student_id]["Marks"]

    if not marks:
        print("Marks not found!")
        return 

    average = sum(marks.values()) / len(marks)
    print(f"\nStudent ID: {student_id}")
    print(f"Average: {average}")

        
# ===================================== FIND TOPPER ======================================
def find_topper():
    highest_avg = 0
    topper = None 

    for student_id , student in students.items():
        marks = student["Marks"]

        if not marks:
            print("Marks not found!")
            return

        average = sum(marks.values()) / len(marks)

        if average > highest_avg:
            highest_avg = average
            topper = student_id

        print(f"\nTopper: {students[topper]["Name"]}")
        print(f"Average: {highest_avg:.2f}")
   

# =============================== SEARCH STUDENT FUNCTION ================================
def search_student():
    student_id = input("Enter student ID: ").upper()

    if student_id in students:
        print(f"\nStudent ID = {student_id}")

        student = students[student_id]

        for key, value in student.items():
            print(f"{key} : {value}")
    else:
        print("Student not found!\n") 

# ================================ DISPLAY GRADE FUNCTION ================================
def display_grade():
    print("-------------------- STUDENT GRADES --------------------")
    for student_id , student in students.items():
        marks = student["Marks"]

        if not marks:
            print(f"ID: {student_id} | Name: {student['Name']} | Grade: N/A")
            continue

        average = sum(marks.values()) / len(marks) 
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"    
        else:
            grade = "F"

        print(f"ID: {student_id} | Name: {student['Name']} | Grade: {grade}")

# ==================================== EXIT FUNCTION =====================================
def exit_program():
    print("Exiting....")

# ==================================== MAIN FUNCTION ====================================
def main():
    is_running = True

    while is_running:
        print("\n--- STUDENT GRADE MANAGER ---\n")
        print("1. Add Student       ")
        print("2. Add Marks         ")
        print("3. View Students     ")
        print("4. Calculate Average ")
        print("5. Find Topper       ")
        print("6. Search Student    ")
        print("7. Display Grade     ")
        print("8. Exit              ")
        print("------------------------------\n")

        choice = input("Enter your choice (1-8): ")

        if not choice.isdigit() or not 1 <= int(choice) <= 8:
            print("Invalid choice! Please choose from 1 to 8.")
            continue

        match choice:
            case "1":
                add_student()
            case "2":
                add_marks()
            case "3":
                view_students()
            case "4":
                calculate_average()
            case "5":
                find_topper()
            case "6":
                search_student()
            case "7":
                display_grade()
            case "8":
                exit_program()
                is_running = False    

        time.sleep(0.5)

if __name__ == '__main__':
    main()                         