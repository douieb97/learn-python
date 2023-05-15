


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'FixedFloat {self.amount:.2f}'

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)

number = FixedFloat(15.5874)
print(number)

new_number = FixedFloat.from_sum(15, 14.2598)
print(new_number)


class Dollar(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'
    
    def __repr__(self):
        return f'<Dollar {self.symbol}{self.amount:.2f}>'
    
mony = Dollar(17.459)
print(mony)
mony = Dollar.from_sum(22.154, 25.258)
print(mony)


print('==========================================')

"""
Class Attributes: Attributes defined outside constructor (__init__)
Class Methods:
    marked with @classmethod decorator
    it take cls parameter not self to point to the class not the instance
    it doesn't require creation of a class instance
    used when you want to do something with the class itself
Static Methods:
    it take no parameters
    its bound to class not instance
    used when doing something doesn't have access to object or class but related to class
"""

class Member:

    # Class Attributes
    not_allowed_names = ['hell', 'shit']
    user_number = 0
    

    def __init__(self, fname, lname, age, gender):
        # Attributes
        self.name = fname + ' ' + lname
        self.age = age
        self.gender = gender
        Member.user_number += 1

    def check_name(self):
        if self.name in Member.not_allowed_names:
            raise ValueError('Name not allowed')
        
    
    def get_name_with_title(self):
        if self.gender == 'male':
            return f'Mr, {self.name}'
        elif self.gender == 'female':
            return f'Miss, {self.name}'
        else:
            return f'{self.name}'
        
    def getinfo(self):
        return f'Hello {self.get_name_with_title()} your full name is {self.name}'

    @classmethod
    def show_users_count(cls):
        return cls.user_number
    
    @staticmethod
    def print():
        print("*" * 50)


member1 = Member('mohammed', 'lougi', 22, 'male')
member1 = Member('mohammed', 'lougi', 22, 'male')
member1 = Member('mohammed', 'lougi', 22, 'male')

print(member1.getinfo())
print(member1.get_name_with_title())
print(Member.user_number)

print(Member.show_users_count())

Member.print()



