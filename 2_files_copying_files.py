


friends = input('Please enter a three friends separated by commas (no space please!): ')
friends = friends.split(', ')
print(friends)

people = open('friends.txt', 'r')

people_nearby = people.readlines()

print(people_nearby[0])


