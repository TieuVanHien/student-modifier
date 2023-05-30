from student import Student

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
            student = Student(input("Please enter the student name: "), input("Please enter the student major: "), input("Please enter the student GPA: "))
            student_list = open("student.txt", "a")
            student_list.write("Name: " + str(student.name) + "\n")
            student_list.write("Major: " + str(student.major) + "\n")
            student_list.write("GPA: " + str(student.gpa) + "\n")
            student_list.write("On Probation: " + str(student.on_probation()) + "\n\n")
            student_list.close()
        if choice == 2:
            student_name = input("Please enter a student name that you want to change information: ")
            update_line = []
            found_student = False
            with open("student.txt", "r") as file:
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
                with open("student.txt", "w") as file:
                    file.writelines(update_line)
                    print("Successfully updated")
                    file.close()
            else:
                print("Failed to update or student not found.")                
        
user_options()
