class House:

    def __init__(self,city, street, house, apartment):
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return (f"city: {self.city} | street: {self.street} | house: {self.house} | apartment: {self.apartment}")

if __name__ == '__main__':
    house1 = House("Gamburg", "Mechnikova", 51, 10)
    house1 = House("Budapesht", "Pushkina", 17, 1)
    house1 = House("Paris", "Timofeeva", 77, 19)

    print(house1)