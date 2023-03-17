class all_staff():
    def __init__(self, name, age, id, birthdate, job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job
    def show(self):
        print(f"{self.id} is {self.name} aged {self.age} birthed in {self.birthdate}, with the job of {self.job}")


class Management(all_staff):
    def __init__(self, name, age, id, birthdate, job, car):
        super().__init__(name, age, id, birthdate, job,)
        self.car = car

    def show(self):
        print(f"{self.id} is {self.name} aged {self.age} birthed in {self.birthdate}, with the job of {self.job}"
              f"and drives a {self.car}")

class Clerical(all_staff):
    def __init__(self, name, age, id, birthdate, job, typing_speed):
        super().__init__(name, age, id, birthdate, job)
        self.typing_speed = typing_speed

    def show(self):
        print(f"{self.id} is {self.name} aged {self.age} birthed in {self.birthdate}, with the job of {self.job}"
              f"and with typing speed of {self.typing_speed}")

class factory(all_staff):
    pass # no unique attribute


# main routine
a = Management('jenne')
