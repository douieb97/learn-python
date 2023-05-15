## Introduction OPP
"""
- Python support object oriented programming
- OOP is a paradigm or coding style
- OOp allow you to organize your code
- Everything in python is object
- Class
    - is the template for creating objects
    - class car can create many cars object
"""


## Example without class
my_student = {
    "name": "otmane",
    "grades": [70, 88, 90, 99]
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))

## Example with class

"""
- Class is the blueprint or constructor of the object
- Class instantiate mean create instance of a class
- Instance is object created from class and have their methods and attributes
- Class define with keyword 'class'
- Class name written with PascalCase style
- Class may contains methods and attributes
- When creating object, python look for the built in method __init__
- __init__ method called every time you create object from class
- __init__ method is initialize data the data for the object
- Any Method with two underscore in the start and end called Dunder method or magic method
- self refer to the current Instance created from the class and must be the first parameter 
- self can be named anything

- Instance attributes defined inside the constructor
- Instance methods take self param which point to instance created from class
- Instance methods can freely access to attributes and methodes in the same object
- Instance methods can access the class itself
"""



# create class Student
class Student:
    # dunder function
    def __init__(self, name, grades):
        # declare properties
        self.name = name
        self.grades = grades
    # declare method
    def average(self):
        return sum(self.grades) / len(self.grades)

# create object from the class Student

student1 = Student('otmane', [70, 88, 90, 99])
student2 = Student('mohammed', [80, 88, 90, 99])
print(student1.average())
print(student2.average())
print(student1.__class__)
print(student2.__class__)

print(Student.average(student1))




