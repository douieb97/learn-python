"""
Lists:
Lists are mutable sequences, typically used to store collections of 
homogeneous items (where the precise degree of similarity will vary 
by application).
"""
## Create a list
students = ['mohammed', 'ayoub', 'ahmad', 'ali']
print(students)
## Access to values with index
print(students[0])
print(students[1])
print(students[2])
print(students[3])
# Reverse access
print(students[-1])
print(students[-2])
print(students[-3])
print(students[-4])
## list in list
products = [
    ["phone", 1500],
    ["pc", 2500],
    ["lamp", 500],
]
print(products)
print(products[0][0])
print(products[2][1])
####################################
print('extend------------------------------')
## extend: Append items from iterable to the end of the list
cars1 = ['bmw', 'opel']
cars2 = ['mercedes', 'dacia']

print(cars1)
cars1.extend(cars2)
print(cars1)
cars1.extend(['vw'])
print(cars1)

print('append------------------------------')
## append: Append a new item with value x to the end of the list.
phone = ['samsung', 'lg']
print(phone)
phone.append('iphone')
print(phone)

print('insert------------------------------')
## insert: Insert a new item with value x in the array before position i.
## Negative values are treated as being relative to the end of the array.
## insert(i, x)

numbers = [1, 2, 3]
print(numbers)
numbers.insert(-10,4)
print(numbers)

print('remove------------------------------')
## remove(x)
## Remove the first occurrence of x from the list.

students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
print(students)
students.remove('ali')
print(students)
students.remove('ali')
print(students)

print('pop------------------------------')
## pop([i])
## Removes the item with the index i from the array and returns it.
## The optional argument defaults to -1, 
## so that by default the last item is removed and returned.

students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
print(students)
last = students.pop()
print(students, last)
students.pop(1)
print(students)

print('del------------------------------')
students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
del students[0:2]
print(students)

print('clear------------------------------')
students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
print(students)
students.clear()
print(students)

print('copy------------------------------')
students1 = ["ali", "ahmad", "mohammed", "otmane", "ali"]
students2 = students1.copy()
print(students2)
students2.clear()
print(students2)
print(students1)

print('count------------------------------')
students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
print(students.count('ali'))
print(students.count('ahmad'))

print('reverse------------------------------')
students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
print(students)
students.reverse()
print(students)

print('sort------------------------------')
students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
print(students)
students.sort()
print(students)

print('len------------------------------')
students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
print(len(students))

print('max and min------------------------------')
students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
print(min(students))
print(max(students))

print(' + ------------------------------')
students1 = ["ali", "ahmad", "mohammed"]
students2 = ["otmane", "ali"]
students = students1 + students2
print(students)

print(' * ------------------------------')
text = ['Python'] * 10
print(text)

print(' in ------------------------------')
students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
print('ahmad' in students)
print('omar' in students)


print('------------------------------')
students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
students[0] = "omar"
print(students)

print('join------------------------------')
students = ["ali", "ahmad", "mohammed", "otmane", "ali"]
commma_separated = ", ".join(students)
print(commma_separated)


