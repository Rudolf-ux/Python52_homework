class Person:
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group

    def __str__(self):
        return (f"name: {self.name} | age: {self.age} | group: {self.group} ")

    def get_gender(self):
        if self.name.endswith('a'):
            return "ж"
        else:
            return "м"



if __name__ == '__main__':
    student_one = Person("Vany", 27, "P52")
    student_two = Person("Karina", 31, "P53")
    student_three = Person("Oleg", 24, "P51")

    print(student_one, student_one.get_gender())
