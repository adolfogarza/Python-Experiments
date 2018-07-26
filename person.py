import time


class Person():
    def __init__(self):
        self.name = "Adolfo"
        self.title = "Platform Software Engineer"
        self.age = 25

    def print_name(self):
        print(self.name)


adolfo = Person()
adolfo.print_name()
