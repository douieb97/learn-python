

## use simple code
car_ages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("car_ages: ", car_ages)
car_ages_descending = sorted(car_ages, reverse=True)
print("car_ages_descending: ", car_ages_descending)
# oldest, second_oldest = car_ages_descending # ValueError: too many values to unpack (expected 2)
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print("oldest: ", oldest)
print("second_oldest: ", second_oldest)
print("others: ", others)


## use catch-all unpacking through a "starred expression"
print('*'*50)
car_ages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
car_ages_descending = sorted(car_ages, reverse=True)
# get first, second, all
oldest, second_oldest, *others = car_ages_descending
print("oldest: ", oldest)
print("second_oldest: ", second_oldest)
print("others: ", others)
# get first, all middles, last
oldest, *others, youngest = car_ages_descending
print("oldest: ", oldest)
print("youngest: ", youngest)
print("others: ", others)
# get from 0 tow second last value, nd last value, last
*others, second_youngest , youngest = car_ages_descending
print("second_youngest: ", second_youngest)
print("youngest: ", youngest)
print("others: ", others)

# *others = car_ages_descending # SyntaxError. You can’t use a catch-all expression on its own


## use multiple starred expressions in an unpacking
print('*'*50)
car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova')
}

print('car inventory items: ', car_inventory.items())
((loc1, (best1, *rest1)), (loc2, (best2, *rest2))) = car_inventory.items()

print(f'Best at {loc1} is {best1}')
print(f'Best at {loc2} is {best2}')

## Unpack short list
print('*'*50)
short_list = [1, 2]
first, second, *rest = short_list
print("first: ", first)
print("second: ", second)
print("rest: ", rest) # return empty list

## unpack iterators
print('*'*50) 
it = iter(range(1, 3))
first, second = it
print("first: ", first)
print("second: ", second)