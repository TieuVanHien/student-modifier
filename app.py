from student import Student
from delete_function import delete_function
from updated_student import Update_student

import json

option = (
    "1. Add Student\n"
    "2. Change Student\n"
    "3. Delete Student\n"
    "4. Exit"
)

def user_options():
    choice = 0
    
    while choice != 4:
        print(option)
        student = []
        try:
            choice = int(input("Enter your choice of action: ")) 
        except ValueError as err:
            print(err)    
            
        if choice == 1:     
            new_student = Student(input("Please enter the student name: "), input("Please enter the student major: "), int(input("Please enter the student GPA: ")))
            with open("student.json", "r+") as file:
                data = json.load(file)
                students = data["student"]
                student_dict = vars(new_student)
                student_dict["probation"] = new_student.on_probation()
                students.append(student_dict)
            
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                file.close()
                print("Successfully added new student!")
        if choice == 2:
            student_name = Update_student(input("Please enter a student name that you want to change information: "))
            found_student = False
            with open("student.json", "r+") as file:
                data = json.load(file)
                students = data["student"]
                for student in students:
                    if student["name"] == student_name:
                        change_student = Student(input("Please enter the updated student name: "), input("Please enter the updated student major: "), int(input("Please enter the updated student GPA: ")))
                        student_dict = vars(change_student)
                        student_dict["probation"] = change_student.on_probation()
                        students.remove(student)  # Remove the old student object
                        students.append(student_dict)
                        found_student = True
                        break    
                        
                if found_student:
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
                    file.close()
                    print("Successfully updated student")
                else:
                    print("Failed to update or student not found.")      
                          
        if choice == 3:
            delete_function()
        
        if choice == 4:    
            print("Thank you")
        
user_options()
