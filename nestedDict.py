students = {
    "stud1": {"name": "kyle", 'age': 18, 'isStudent': True},
    "stud2": {"name": "vhon", 'age': 19, 'isStudent': True},
    "stud3": {"name": "gab", 'age': 18, 'isStudent': True},
    "stud4": {"name": "jhed", 'age': 19, 'isStudent': True}
    
}
students_2 = {
    "stud5": {"name": "yu", 'age': 18, 'isStudent': True},
    "stud6": {"name": "me", 'age': 19, 'isStudent': True},
    "stud7": {"name": "he", 'age': 18, 'isStudent': True},
    "stud8": {"name": "she", 'age': 19, 'isStudent': True}
}
for key in students:
    print(key, ":", students[key])
    
#print(students.keys()) #return only the keys on the dict
#print(students.values()) # return only the values (per key)
#print(students.items()) # return all (key and elements)
#print(students.get("stud1"))

print()
print("after adding another dict: ")
students.update(students_2) # combining two dictionaries
for key in students:
    print(key, ":", students[key])

print()
print("After modifying:")
print()

# adding another element to the dict
students["stud5"] = {"name": "cyril", 'age': 18, 'isStudent': True}
students.pop("stud5") # pop using a specific key
students.popitem() # pop the last item

for key in students:
    for k in students[key]:
        print( students[key][k], end = " ")
    print()
print()
for key in students:
    for k in students[key]:
        if k == "name":
            print( students[key][k], end = " ")
            break
    print()

