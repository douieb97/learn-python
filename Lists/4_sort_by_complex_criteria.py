## Simple Sort
numbers = [100, 99, 78, 1001, 45, 15, 1]
print(numbers)
numbers.sort()
print(numbers)



print('*'*50)

class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'
    

tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25),
]

"""
Sorting objects of this type doesn’t work because the sort method 
tries to call comparison special methods that aren’t defined by the 
class
"""
# tools.sort() # TypeError: '<' not supported between instances of 'Tool' and 'Tool'

"""
there’s an attribute on the object that you’d like to use for sorting. To support this use case, the sort method accepts a key parameter that’s expected to be a function. The key function is passed a 
single argument, which is an item from the list that is being sorted. 
The return value of the key function should be a comparable value 
(i.e., with a natural ordering) to use in place of an item for sorting 
purposes.
"""

"""
Here, I use the lambda keyword to define a function for the key parameter that enables me to sort the list of Tool objects alphabetically by 
their name:
"""

print("Unsorted: ", repr(tools))
tools.sort(key= lambda x: x.name)
print("Sorted: ", repr(tools))








