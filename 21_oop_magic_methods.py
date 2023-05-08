

class Student:
    def __init__(self, name):
        self.name = name


movies = ['Matrix', 'Finding Nemo']

## __class__: The class to which a class instance belongs.
print(movies.__class__)

## __len__
class Garage:
    def __init__(self):
        self.cars = []

ford = Garage()
ford.cars.append("focus")
ford.cars.append("fiesta")
# print(len(ford))  TypeError: object of type 'Garage' has no len()
# to fix that add __len__
class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)

ford = Garage()
ford.cars.append("focus")
ford.cars.append("fiesta")
print(len(ford))


## __getitem__

class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)

ford = Garage()
ford.cars.append("focus")
ford.cars.append("fiesta")
print(len(ford))
# print(ford[0]) TypeError: 'Garage' object is not subscriptable
# to fix that use __getitem__

class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, index):
        return self.cars[index]

ford = Garage()
ford.cars.append("focus")
ford.cars.append("fiesta")
print(len(ford))
print(ford[0])
print(dir(ford))

## __repr__
# Called by the repr() built-in function to compute the “official” 
# string representation of an object. The return value must be a string object.

class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, index):
        return self.cars[index]
    
    def __repr__(self):
        return f'<Garage {self.cars}>'

ford = Garage()
ford.cars.append("focus")
ford.cars.append("fiesta")
print(len(ford))
print(ford[0])
print(repr(ford))

## __str__

class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, index):
        return self.cars[index]
    
    def __repr__(self):
        return f'<Garage {self.cars}>'
    
    def __str__(self):
        return f'Garage with {len(self.cars)} cars'

ford = Garage()
ford.cars.append("focus")
ford.cars.append("fiesta")
print(len(ford))
print(ford[0])
print(repr(ford))
print(str(ford))


