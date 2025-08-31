class car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.name} {self.model}"
    

carName = input("What is the brand of your car: ")
carModel = input("What is the model of your car: ")
carYear = input("What is the manufacturing year of your car: ")
myCar = car(carName, carModel, carYear)
print("Your car is: ", myCar.display_info())