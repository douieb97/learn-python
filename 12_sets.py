## Sets

students = {"otmane", "ayoub", "mohammed", "otmane"}
print(len(students))

print('add-------------------------------')
students = {"otmane", "ayoub", "mohammed", "otmane"}
students.add('ali')
print(students)
print(len(students))

print('remove-------------------------------')
students = {"otmane", "ayoub", "mohammed", "otmane"}
students.remove('mohammed')
print(students)
print(len(students))

print('difference-------------------------------')
students_art = {"otmane", "ayoub"}
students_math = {"mohammed", "otmane"}

art_but_not_math = students_art.difference(students_math)
print(art_but_not_math)

print('symmetric_difference-------------------------------')
students_art = {"otmane", "ayoub"}
students_math = {"mohammed", "otmane"}

not_in_both = students_art.symmetric_difference(students_math)
print(not_in_both)

print('symmetric_difference-------------------------------')
students_art = {"otmane", "ayoub"}
students_math = {"mohammed", "otmane"}

art_and_math = students_art.intersection(students_math)
print(art_and_math)

print('union-------------------------------')
students_art = {"otmane", "ayoub"}
students_math = {"mohammed", "otmane"}

all = students_art.union(students_math)
print(all)


