class Student:
    def __init__(self, name, age, phone_number, form_class, subjects, is_male):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = is_male
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
    # available form classes are: "BAKER", "MORGAN", "MCNICOL", "GRAHAM", "BELL", "NIMMO", "BARKER"
    # available classes are: "ART", "ENG", "MAT", "GRA", "DTC", "PHY", "BIO"
    import csv
    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[5] == "True":
                is_male = True
            else:
                is_male = False
            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)

def count_students():
    class_to_search = input("what class are you looking for?: ")

# Main routine

student_list = []
generate_students()

print_Student_detals()
#selected_student_age()
