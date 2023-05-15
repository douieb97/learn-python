
class Member:
    def __init__(self, fname, lname, age, gender):
        # Attributes
        self.name = fname + ' ' + lname
        self.age = age
        self.gender = gender
    
    def get_name_with_title(self):
        if self.gender == 'male':
            return f'Mr, {self.name}'
        elif self.gender == 'female':
            return f'Miss, {self.name}'
        else:
            return f'{self.name}'
        
    def getinfo(self):
        return f'Hello {self.get_name_with_title()} your full name is {self.name}'

## Inheritance
class VipMember(Member):
    def __init__(self, fname, lname, age, gender, vip_id):
        super().__init__(fname, lname, age, gender)
        self.vip_id = vip_id


class GymPass:
    def __init__(self, gym_pass_id):
        self.gym_pass_id = gym_pass_id

## Multi Inheritance
class ExtraMember(VipMember, GymPass):
    pass
    

member1 = Member('mohammed', 'lougi', 22, 'male') 

print(member1.getinfo())
print(member1.get_name_with_title())

ex = ExtraMember()