class Student:
    def __init__(self, name, age, phone_number, form_class, subjects):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = True
        self.enrolled = True
        self.student_details = student_list.append(self)

    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.phone_number)
        print(self.form_class)
        print(self.subjects)
        print(self.is_male)
        print(self.enrolled)


def selected_student_age():
    age = int(input("what's your age: "))
    for student in student_list:
        if student.age >= age:
            student.display_info()


def print_Student_detals():
    for student in student_list:
        student.display_info()



# Main routine
# Students
student_list = []
Student("Karen", 17, "123-4567", "WNLR", "13 DTC, 13SMX")
Student("Bob", 18, "021-0263674", "BNNL", "13SMX")
Student("Lisa", 16, "022-4567123", "SKWR", "13DTC, 13SMX")
Student("Patrick", 18, "023-01234567", "SCBE", "13ENg, 13CMX, 13SMX, 13DTC")
#print_Student_detals()
selected_student_age()
