import json

def delete_student():
    student_name = input("Please enter a student name that you want to delete: ")
    update_lines = []
    found_student = False
    
    with open("student.json", "r") as file:
        data = json.load(file)
        for student in data["student"]:
            name = student["name"]
            if name.startswith(student_name):
                found_student = True
            else:
                update_lines.append(student)
    
    if found_student:
        with open("student.json", "w") as file:
            json.dump(update_lines, file)
        print("Successfully deleted.")
    else:
        print("Failed to delete or student not found.")

# def print_json():
#     with open("student.json", "r") as file:
#         data = json.load(file)
#         for student in data["student"]:
#             name = student["name"]
#             print(name)
    
# print_json()    