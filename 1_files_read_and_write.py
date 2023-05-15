#! python3
import os

cwd = os.getcwd()
filepath = os.path.join(cwd, 'data.txt')

## Read file

file = open(filepath, 'r')

content = file.read()

print(content)

file.close()

## Write file

file = open(filepath, 'w')

file.write('My name is otmane')

file.close()


