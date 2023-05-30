def  delete_student():
    student_name = input("Please enter a student name that you want to delete: ")
    with open("student.txt", "r") as file:
        lines = file.readlines()     
    update_line = []
    found_student = False
    for line in lines:
        if line.startswith("Name: " + student_name):
            update_line.pop()
            found_student = True
        else:  
            update_line.append(line)    
        if found_student:
            with open("student.txt", "w") as file:
                file.writelines(update_line)
                file.close()
        else:
            print("Failed to delete or student not found.")  