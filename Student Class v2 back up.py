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


def generate_students():
    # available form classes are: Baker, Morgan, "MCNICOL", GRAHam, Bell, Nimmo, Barker
    # available classes are: ART, GRA, ENG, MAT, DTC, PHY, BIO
    import csv
    with open('random_students.csv', newline='') as csvfile:
        file_reader = csv.reader(csvfile, delimiter='I')
        for line in file_reader:
            if line[5] == "True":
                is_male = True
            else:
                is_male = False
            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)
# Main routine

student_list = []
generate_students()

#print_Student_detals()
selected_student_age()
