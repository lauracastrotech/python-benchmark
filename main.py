# Beneath each comment write the code and print out the result to check it works
import math

'''LISTS'''

# Create a list and assign it to a variable
a_list = [1, 2, 3]

# Find the length of the list
len(a_list)

# Append an item to the list
a_list.append(4)

# Find the value of an item in the list a specific index
a_list[1]

# Set the value of an item at a specific index
a_list[1] = 5

# Check whether an item is in the list
in_list = 5 in a_list

# Sort the list???????????????

# Iterate over the list using range, printing out each element and the index
for idx in range(len(a_list)):
    print(a_list[idx])

# Iterate over the list without using range, printing out each element
for item in a_list:
    print(item)

'''TUPLES'''

# Create a tuple and assign it to a variable
a_tup = (1, 3, )
# Find the length of the tuple
len(a_tup)

# Find the value of an item in the tuple a specific index
a_tup[0]

# Check whether an item is in the tuple
1 in a_tup

# Iterate over the tuple using range, printing out each element and the index
for idx in range(len(a_tup)):
    print(a_tup[idx])

# Iterate over the tuple without using range, printing out each element
for item in a_tup:
    print(item)

'''STRINGS'''

# Create a string and assign it to a variable
a_string = 'Hello World!'

# Find the length of the string
len(a_string)

# Find the value of an character in the string a specific index
a_string[3]

# Check whether an item is in the string
'Hello' in a_string

# Concatenate (add) two strings together
'Hello ' + 'Moon!'

# Create an f-string
f'{a_string}'

# Split a string using .split
a_string.split()

# Join a list of strings using .join?????????????
# a_string.join(*)


# Iterate over the string using range, printing out each character and the index
for char in range(len(a_string)):
    print(f'{a_string[char]} is at index: {[char]}')

# Iterate over the string without using range, printing out each character
for char in a_string:
    print(char)

'''DICTIONARIES'''

# Create a dictionary and assign it to a variable
a_dict = {
    'hello': 5,
    'world': 5
}

# Find the length of the dictionary
len(a_dict)

# Add a new key/value pair
a_dict['!'] = 1

# Replace value for a given key
a_dict['world'] = 4

# Check whether a key is in the dictionary
'world' in a_dict

# Iterate over keys, printing each key
for key in a_dict.keys():
    print(key)

# Iterate over over key/value pairs using .items(), printing each key and value
for key, value in a_dict.items():
    print(f'{key} {value}')

'''SETS'''

# Create a set and assign it to a variable
a_set = set()

# Find the length of the set
len(a_set)

# Add a new element
a_set.add(78)
a_set.add(32)

# Remove an element
a_set.remove(32)

# Check whether a element is in the set
78 in a_set

# Iterate over elements, printing each one out
for el in a_set:
    print(el)

'''NUMBERS'''

# Add / subtract / multiply 2 numbers
addition = 4+5
subtraction = 5-4
multiplication = 4*5

# Divide two numbers using normal (float) division
f_division = 4/2
print(f'{f_division=}')

# Divide two numbers using integer division
i_division = 9//3
print(f'{i_division=}')

# Find the modulo (remainder) of two numbers
modulo = 12/5
print(f'{modulo=}')

# Check whether a number is even/odd
a_number = 'Even' if 8 % 2 == 0 else 'Odd'
print(a_number)

# Round a float down to an int
a_float = 2.3
print(math.floor(a_float))

'''FUNCTIONS'''

# Write a function that takes no arguments and call it
def call_a_func():
    print('This calls a function.')
call_a_func()
# Write a function that takes one or more arguments and call it
def a_func_arg(arg1):
    print(arg1)
a_func_arg(78)
# Write a function that returns a value. Call the function and store the return value in a variable
def a_func_returns():
    return 'a value'
a_var = a_func_returns()
print(f'{a_var=}')

'''LOOPS'''

# Write a while loop
count = 3
while count > 0:
    print(count)
    count -= 1
# Write a for loop that loops a set number of times (e.g. 10 times)
for num in range(10):
    print(num)

'''CONDITIONALS'''

# Write an if/elif/else statement
something = 'something'
if not something:
    print("nothing")
elif something:
    print(something)
else:
    print('whatever')
# Write conditionals for the following operators:
num1 = 45
num2 = 30
num3 = 30
# ==
num1==num2
# !=
num1!=num2
# <
num1<num2
# >
num1>num2
# <=
num2<=num3
# >=
num3>=num2

'''NESTED DATA'''

# Write a nested list (a list of lists) and assign it to a variable
list_of_lists = [[2,3], [4,5,6]]

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second
print(list_of_lists[0][1])

# Iterate through the nested data structure using range
for i in range(len(list_of_lists)):
    for j in range(len(list_of_lists[i])):
        print(list_of_lists[i][j])

# Iterate through the nested data structure without using range 
for i in list_of_lists:
    for j in i:
        print(j)

'''REMINDER'''

# You're doing great and you got this!
