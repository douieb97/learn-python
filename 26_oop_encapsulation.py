"""
Encapsulation: restrict access to the data stored in attributes and methods
* public
every attribute and method that we used so far is public
attributes and methods can be modified and run from everywhere inside or outside the class
* Protected
attributes and methods can be accessed from within the class and sub classes
attributes and methods prefixed with one underscore _
* private
attributes and methods can be accessed from within the class or object only
attributes cannot be modified from outside the class
attributes and methods prefixed with two underscore __

"""

## Public
class Member:
    def __init__(self, name):
        self.name = name


member1 = Member('Ahmad')
print(member1.name)
member1.name = "Mohammed"
print(member1.name)

## Protected
class Member:
    def __init__(self, name):
        self._name = name


member1 = Member('Ahmad')

## Private
class Member:
    def __init__(self, name):
        self.__name = name

    def say_hello(self):
        return(f'Hello {self.__name}')


member1 = Member('Ahmad')
# print(member1.__name) Error
# bypass
# print(member1._Member__name)
print(member1.say_hello())
