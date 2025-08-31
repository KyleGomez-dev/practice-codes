#Creating a object and putting them into a list.

class pearson:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, gender: {self.gender}")
    

person1 = pearson("Alice",16,'female')

person1.display_info()
