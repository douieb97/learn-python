## Strings

text1 = "This is a string"
print(text1)

text2 = 'This is a string'
print(text2)

text3 = """
This 
is 
a 
string
"""
print(text3)

print('Functions----------------------------')
print('len----------------------------')
## len: get number of characters
name = 'otmane'
print(len(name))

print('reverse characters----------------------------')
name = 'otmane'
print(name[::-1])

print('find----------------------------')
name = 'my name is otmane'
find = name.find('otmane')

print(find)

print('in----------------------------')
name = 'my name is -otmane-'
print('otmane' in name)
print('otmanes' in name)

print('split----------------------------')
text = 'This is a string'
list1 = text.split()
print(list1)
list2 = text.split('i')
print(list2)


print('replace----------------------------')
text1 = 'This is a string'
text2 = text1.replace('string', '****')
print(text1)
print(text2)


