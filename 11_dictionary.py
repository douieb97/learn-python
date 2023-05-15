## Dictionaty

students = {
    'id001': 'otmane',
    'id002': 'mohammed',
    'id003': 'omar',
    'id004': 'ahmad'
}

print(students)
print(students['id001'])
print(students.keys())
print(students.values())
print(students.items())

print("get---------------------------")
students = {
    'id001': 'otmane',
    'id002': 'mohammed',
    'id003': 'omar',
    'id004': 'ahmad'
}
print(students.get('id002'))
print(students.get('id004'))

print("in---------------------------")
students = {
    'id001': 'otmane',
    'id002': 'mohammed',
    'id003': 'omar',
    'id004': 'ahmad'
}
print('id004' in students)
print('ahmad' in students)
print('id005' in students)

print("repr---------------------------")
students = {
    'id001': 'otmane',
    'id002': 'mohammed',
    'id003': 'omar',
    'id004': 'ahmad'
}
print(repr(students))

print("update---------------------------")
students = {
    'id001': 'otmane',
    'id002': 'mohammed',
    'id003': 'omar',
    'id004': 'ahmad'
}

students.update({'id004': 'ayoub'})
print(students)
students.update({'id001': 'youssef'})
print(students)

print("for---------------------------")
students = {
    'id001': 'otmane',
    'id002': 'mohammed',
    'id003': 'omar',
    'id004': 'ahmad'
}

for key, value in students.items():
    print('User id ' + key + ' is ' + value)

print("convert list to dictionary---------------------------")
students = [
    ('id001', 'otmane'),
    ('id002', 'mohammed'),
    ('id003', 'omar'),
    ('id004', 'ahmad')
]
print(students)
print(dict(students))