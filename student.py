class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def on_probation(self):
        if self.gpa < 2.0:
            return True
        else:
            return False    