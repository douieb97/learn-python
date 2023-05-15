## List comprehension

# Use for only
numbers = [0, 1, 2, 3, 4]
doubled_numbers = []
for _ in numbers:
    doubled_numbers.append(_ * 2)
print(doubled_numbers)

# Use list comprehension
doubled_numbers = [_ * 2 for _ in numbers]
print(doubled_numbers)

ages = [22, 35, 27, 21, 20]
odds = [_ for _ in ages if _ % 2 == 1]
print(odds)
