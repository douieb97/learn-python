"""
ord(character):
Given a string representing one Unicode character,
return an integer representing the Unicode code point of that character
"""
print(ord('1'))

l = list(range(ord('a'), ord('z')))
print(l)

"""
char(integer)
Return the string representing a character whose Unicode code 
point is the integer i
"""

print(chr(1))


# Example with range
start = '1'
end = '9'
for i in range(ord(start), ord(end)):
    print(chr(i))

for i in range(2000, 5000):
    print(chr(i) + " => " + str(i))
