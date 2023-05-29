from student import Student
from choice import Choice

def student_modifier():
    student = Student(input("Please enter the student name: "), input("Please enter the student major: "), input("Please enter the student GPA: "))
    student_list = open("student.txt", "a")
    student_list.write("Name: " + str(student.name) + "\n")
    student_list.write("Major: " + str(student.major) + "\n")
    student_list.write("GPA: " + str(student.gpa) + "\n")
    student_list.write("On Probation: " + str(student.on_probation()) + "\n\n")
    student_list.close()
    
student_modifier()             

    
   