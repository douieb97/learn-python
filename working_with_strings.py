## Escape Characters
print("Escape Characters" + "=" * 30)
print("Hello there!\nHow are you?\nI\'m doing fine.")

## Raw Strings
print("Raw Strings" + "=" * 30)
print(r"Hello there!\nHow are you?\nI\'m doing fine.")

## Multiline Strings
print("Multiline Strings" + "=" * 30)
print("""
Dear Alice,
This is a multiline string
thanks
""")

## Indexing and slicing strings
print("Indexing and slicing strings" + "=" * 30)
text = "Hello world"
# get first character
print(text[0])
# get last character
print(text[-1])
# get first five characters
print(text[:5])
print(text[0:5]) # from text[0] to text[4]

## The in and not in Operators with Strings
print("The in and not in Operators with Strings" + "=" * 30)
text = "Hello world!"

print('' in text)
print('hello' in text) # case sensitive
print('Hello' in text)
print(' ' in text)

## String Methods
print("String Methods" + "=" * 30)
# upper and lower
text = "Hello world!"
print(f"Original: {text}")
print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
# islower and isupper
text = 'alice'
print(text.islower())
text = 'Alice'
print(text.islower())
text = 'ALICE'
print(text.isupper())
text = 'Alice'
print(text.isupper())

# for more isX string: isalnum, isalpha ...
"""
isalpha() returns True if the string consists only of letters and is not blank.
isalnum() returns True if the string consists only of letters and numbers and
is not blank.
isdecimal() returns True if the string consists only of numeric characters
and is not blank.
isspace() returns True if the string consists only of spaces, tabs, and
newlines and is not blank.
istitle() returns True if the string consists only of words that begin with
an uppercase letter followed by only lowercase letters.
"""

# startswith and endswith
print('startswith & endswith')
text = 'Hello World!'
print(text.startswith(''))

# join and split
print('join and split' + "=" * 30)
print(''.join(['H','e','l','l','o']))
print(', '.join(['H','e','l','l','o']))
print(' '.join(['H','e','l','l','o']))

print('Hello world!'.split())
print('HelloABCworld!'.split('ABC'))

# rjust, ljust, and center
print('join and split' + "=" * 30)

print('Hello'.rjust(20))
print('Hello'.rjust(20, '-'))

print('Hello'.ljust(20))
print('Hello'.ljust(20, '-'))

print('Hello'.center(20))
print('Hello'.center(20, '-'))

# strip, rstrip, and lstrip
print('strip, rstrip, and lstrip' + "=" * 30)

text = '  Hello world  '
print(len(text))
print(text.strip())
print(len(text.strip()))

text = '  Hello world  '
print(len(text))
print(text.lstrip())
print(len(text.lstrip()))

text = '  Hello world  '
print(len(text))
print(text.rstrip())
print(len(text.rstrip()))

text = 'Hello world'
print(text.strip('Hello'))

## Copying and Pasting Strings with the pyperclip
print('Copying and Pasting Strings with the pyperclip' + "=" * 30)








