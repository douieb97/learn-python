## Tuples
students = ("ali", "ahmed", "otmane", "omar")
print(students)
print(students[0])

print('--------------------------------')
name1, name2, name3 = ("ali", "ahmed", "otmane")
print(name1)
print(name2)
print(name3)

print('* --------------------------------')
name = ("Python_") * 10
print(name)

print('+ --------------------------------')
students1 = ("ali", "ahmed")
students2 = ("otmane", "omar")
students = students1 + students2
print(students)

print('min and max and in --------------------------------')
students = ("ali", "ahmed", "otmane", "omar")
print(min(students))
print(max(students))
print("otmane" in students)