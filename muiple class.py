class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # an interger between 1 - 100

    def print_details(self): # crete a method to display the imformations
        return f"{self.name} is a {self.colour} dog aged {self.age}"




class course:
    def __init__(self, name, max_students,):
        self.name = name
        self.max_students = max_students
        self.students = []  # blank list to hold the students


    def add_students(self, students):
        # Test there is room in the course
        if len(self.students) < self.max_students:
            self.students.append(students)
            return True
        return False


    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.gett_grade()
        return total / len(self.students)


# Instantiate 3 student objects
S1 = student("TIm", 19, 95)
S2 = student('Joy', 19, 75)
S3 = student("Jill", 19, 65)

# Instantiate course object
cours1 = course("computer science", 3)  # Test the list if try tto put more than 2

# add students to course
cours1.add_students(S1)
cours1.add_students(S2)
cours1.add_students(S3)

# Get average grade
print(f"The avearge grade in {cours1.name} is {cours1.get_average_grade()}")
