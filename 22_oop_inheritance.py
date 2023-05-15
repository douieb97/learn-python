## Inheritance

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    def show_info(self):
        print(f"Name:{self.name}\nSchool:{self.school}")


class WorkingStudent(Student):
    
    ## Use Derived class Name
    def __init__(self, name, school, salary):
        Student.__init__(self, name, school)
        self.salary = salary

    ## Use super keyword
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.5
    
    ## Overriding show_info method
    def show_info(self):
        print(f"Name:{self.name}\nSchool:{self.school}\nSalary:{self.salary}")

rolf = WorkingStudent('rolf', 'MIT', 15.50)
print(rolf.salary)
print(rolf.name)
print(rolf.marks)
rolf.marks.append(15)
rolf.marks.append(80)
rolf.marks.append(60)
print(rolf.average())
print("*"*50)
alan = WorkingStudent("aln", 'ASG', 19.50)
rolf.show_info()
alan.show_info()
