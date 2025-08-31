#Creating a object and putting them into a list.
class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def hello(self):
        print(f"Hello I'm {self.name},{self.age} years old, and my gender is {self.gender}")
        
        
p1 = person('kyle',18,'male')
p2 = person('gab',18,'male')
p3 = person('vhon',19,'male')
p4 = person('jhed',19,'male')



arr = [p1,p2,p3,p4]

for arrs in arr:
    arrs.hello()
    if arrs == p2:
        print('gab is detected, stopping the loop.')
        break

print(type(arrs))
