class Student():
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    def name(self):
        return self.firstname + " " + self.surname
        student = Student("Monika", "Mustermann")
print(student.name())