class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(self.brand, self.year)

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def info(self):
        print(self.brand, self.year, self.model)

v1 = Vehicle("Toyota", 2020)
c1 = Car("Toyota", 2022, "Corolla")

v1.info()
c1.info()
