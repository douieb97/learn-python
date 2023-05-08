## Example without class
my_student = {
    "name": "otmane",
    "grades": [70, 88, 90, 99]
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))

## Example with class

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


