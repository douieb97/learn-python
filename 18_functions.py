## Functions

# Create function

def hello():
    print('hello world!')
# Call function
hello()

# Arguments and parameters

def hello(name):
    print(f'Hello {name}')
    
hello('otmane')


# Example

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    res = f"{car['make']} {car['model']}"
    print(f'{res} does {mpg} miles per gallon')


for car in cars:
    calculate_mpg(car)


# Return
print('--------------------------')
cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg

for car in cars:
    print(calculate_mpg(car))

# Default parameter value

def add(x=0, y=0):
    total = x + y
    return total

print(add())
print(add(1,2))
print(add(y=5)) # names parameter

print('--------------------------')

# Lambda function

add = lambda x, y: x + y
print(add(1, 2))

print((lambda x, y: x + y)(15, 3))








