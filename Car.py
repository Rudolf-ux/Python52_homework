class Car:

    def __init__(self, car_number, model, color, horsepower):
        self.car_number = car_number
        self.model = model
        self.color = color
        self.horsepower = horsepower

    def __str__(self):
        return (f"car_number: {self.car_number} | model:{self.model} | color: {self.color} | horsepower: {self.horsepower}" )

    def calculate_recycling_fee(self):

        base_fee = 1000
        power_coefficient = self.horsepower / 100
        recycling_fee = base_fee * self.horsepower
        return recycling_fee

    def calculate_vehicle_tax(self):

        tax_rate = 15  # Ставка налога за 1 лошадиную силу
        vehicle_tax = self.horsepower * tax_rate
        return vehicle_tax

    def calculate_vehicle_tax(self):

        tax_rate = 15
        vehicle_tax = self.horsepower * tax_rate
        return vehicle_tax

if __name__ == '__main__':
    car1 = Car("O161OO161", "VAZ", "Black", 550)
    car2 = Car("O111OO761", "GAZ", "Black", 555)
    car3 = Car("B161OP061", "YAZ", "Black", 450)

    print(car3, f" | recycling: {car1.calculate_recycling_fee()} | vehicle: {car1.calculate_vehicle_tax()} ")