import json
from delete_student import Delete_student

def delete_function():
    student_name = Delete_student(input("Please enter a student name that you want to delete: "))
    found_student = False

    with open("student.json", "r+") as file:
        data = json.load(file)
        students = data["student"]
        line = []
        for student in students:
            if student["name"] == student_name:
                students.remove(student)
                found_student = True
                break
            else:
                students.append(line)

        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
        file.close()

    if found_student:
        print("Successfully deleted.")
    else:
        print("Student not found.")