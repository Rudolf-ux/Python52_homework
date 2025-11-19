from Person import Person
from Car import Car
from House import House


def main():

    person = Person("Anna", 25, 52)
    car = Car("Toyota", "Camry", "black", 550)
    house = House("Moscow", "Malinki", 10, 5 )

    print(person)
    print(car)
    print(house)


if __name__ == '__main__':
    main()