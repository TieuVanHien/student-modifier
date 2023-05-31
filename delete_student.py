import json

def delete_student():
    student_name = input("Please enter a student name that you want to delete: ")
    found_student = False

    with open("student.json", "r+") as file:
        data = json.load(file)
        students = data["student"]
        for student in students:
            if student["name"] == student_name:
                students.remove(student)
                found_student = True
                break

        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

    if found_student:
        print("Successfully deleted.")
    else:
        print("Student not found.")