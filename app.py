from student import Student

option = (
    "1. Add Student\n"
    "2. Change Student\n"
    "3. Delete Student\n"
    "4. Exit"
)

def user_options():
    choice = 0
    print(option)
    try:
        choice = int(input("Enter your choice of action: ")) 
    except ValueError as err:
        print(err)    
    while choice != 4:    
        if choice == 1:
            def student_modifier():
                student = Student(input("Please enter the student name: "), input("Please enter the student major: "), input("Please enter the student GPA: "))
                student_list = open("student.txt", "a")
                student_list.write("Name: " + str(student.name) + "\n")
                student_list.write("Major: " + str(student.major) + "\n")
                student_list.write("GPA: " + str(student.gpa) + "\n")
                student_list.write("On Probation: " + str(student.on_probation()) + "\n\n")
                student_list.close()  
            student_modifier() 
                                
user_options()


    
          

    
   