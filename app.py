from student import Student
from delete_student import delete_student
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
            new_student = Student(input("Please enter the student name: "), input("Please enter the student major: "), input("Please enter the student GPA: "))
            with open("student.json", "r+") as file:
                data = json.load(file)
                students = data["student"]
                student_dict = vars(new_student)
                student_dict["probation"] = new_student.on_probation()
                students.append(student_dict)
            
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
     
        if choice == 2:
            student_name = input("Please enter a student name that you want to change information: ")
            update_line = []
            found_student = False
            with open("student.json", "r") as file:
                for line in file:
                    if line.startswith("Name: " + student_name):
                        student = Student(input("Please enter the updated student name: "), input("Please enter the updated student major: "), input("Please enter the updated student GPA: "))
                        update_line.append("Name: " + str(student.name) + "\n")
                        update_line.append("Major: " + str(student.major) + "\n")
                        update_line.append("GPA: " + str(student.gpa) + "\n")
                        update_line.append("On Probation: " + str(student.on_probation()) + "\n\n")
                        found_student = True
                        # skip until the next blank line
                        for line in file:
                            if line == '\n':
                                break
                    else:
                        update_line.append(line)
                   
            if found_student:
                with open("student.json", "w") as file:
                    file.writelines(update_line)
                    print("Successfully updated")
                    file.close()
            else:
                print("Failed to update or student not found.")      
                          
        if choice == 3:
            delete_student()
        
        if choice == 4:    
            print("Thank you")
        
user_options()
