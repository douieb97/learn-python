## Know How to Slice Sequences

"""
From x to y
[x:y]
start: start from index x
end: end in index y-1
"""
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(alpha[3:5]) # start from index 3 to index 5-1 => ['d', 'e']
print(alpha[1:7]) # return ['b', 'c', 'd', 'e', 'f', 'g']

"""
From 0 to y
[0:y] or [:y]
start: start from index 0
end:  end in index y-1
"""
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(alpha[0:5]) # return ['a', 'b', 'c', 'd', 'e']
print(alpha[:5])  # return ['a', 'b', 'c', 'd', 'e']

"""
From x to end
[x:len(list)] or [x:]
start: start from index x
end: end in index (list length-1) 
"""
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(alpha[2:len(alpha)]) # return ['c', 'd', 'e', 'f', 'g', 'h']
print(alpha[2:]) # return ['c', 'd', 'e', 'f', 'g', 'h']

"""
From start to end
[:]
start: start from index 0
end: end in index (list length-1) 
"""
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(alpha[:])

"""
From start to before last
[x:-1]
"""
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(alpha[:-1]) # return ['a', 'b', 'c', 'd', 'e', 'f', 'g']

"""
Last x items
[-x:]
"""
""" index -8  -7   -6   -5   -4   -3   -2   -1   """
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(alpha[-3:]) # return ['f', 'g', 'h']

""" Examples
a[:]     # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:5]    # ['a', 'b', 'c', 'd', 'e']
a[:-1]   # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
a[4:]    #                     ['e', 'f', 'g', 'h']
a[-3:]   #                          ['f', 'g', 'h']
a[2:5]   #           ['c', 'd', 'e']
a[2:-1]  #           ['c', 'd', 'e', 'f', 'g']
a[-3:-1] #                          ['f', 'g']
"""

# use assignments
print("*"*30)

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("Before: ", alpha)
alpha[2:7] = [99, 22, 14]
print("After: ", alpha) # show ['a', 'b', '99', '22', '14', 'h']

print("*"*30)
print("Before: ", alpha)
alpha[2:3] = [47, 11] # show ['a', 'b', 47, 11, 22, 14, 'h']

print("*"*30)
# list[:]  vs list
print("alpha ", alpha)
b = alpha[:]
print("b ", b)

assert b == alpha and b is not alpha

b = alpha
assert b == alpha and alpha is b # True

print("Before alpha: ", alpha)
print("Before b    : ", b)
alpha[:] = [101, 102, 103]
assert alpha is b # True
print("After alpha: ", alpha)
print("After b    : ", b)
