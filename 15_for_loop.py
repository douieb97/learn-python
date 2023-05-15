## For loop

# for loop with list
students = ["otmane", "ahmad", "amin", "omar"]

for student in students:
    print(student)

# for loop with dictionary

students = {
    "id001": "otmane",
    "id002": "ahmad",
    "id003": "amin",
    "id004": "omar",
}

for index, value in students.items():
    print(f"Student id: {index}, name is {value}")