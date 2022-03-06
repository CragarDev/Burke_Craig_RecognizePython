num1 = 42  # - variable declaration | - Data Types- Primitive- Numbers
num2 = 2.3  # - variable declaration | - Data Types- Primitive- Numbers
boolean = True  # - variable declaration | - Data Types- Primitive- Boolean
string = 'Hello World'  # - variable declaration | - Data Types- Primitive- Strings
# - variable declaration | - Data Types- Composite - List - initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}  # - variable declaration | - Data Types - Composite - Dictionary - initialize
# - variable declaration | - Data Types - Composite - Tuples - initialize
fruit = ('blueberry', 'strawberry', 'banana')
# - log statement | - type check | - Data Types - Composite - Tuples - access value
print(type(fruit))
# - log statement | - Data Types - Composite - List - access value
print(pizza_toppings[1])
# - Data Types - Composite - List - change value - add value
pizza_toppings.append('Mushrooms')
# - log statement | - Data Types - Composite - Dictionary - access value
print(person['name'])
# - Data Types - Composite - Dictionary - access value - change value
person['name'] = 'George'
# - Data Types - Composite - Dictionary - access value - add value
person['eye_color'] = 'blue'
# - log statement | - Data Types - Composite - Tuples - access value
print(fruit[2])

if num1 > 45:  # - conditional - if
    print("It's greater")  # - log statement
else:  # - conditional - else
    print("It's lower")  # - log statement

if len(string) < 5:  # - length check | - conditional - if
    print("It's a short word!")  # - log statement
elif len(string) > 15:  # - length check | - conditional - else if
    print("It's a long word!")  # - log statement
else:  # - conditional - else
    print("Just right!")  # - log statement

for x in range(5):  # - for loop - start - increment - stop
    print(x)  # - log statement | - for loop - stop
for x in range(2, 5):  # - for loop - start - increment - stop
    print(x)  # - log statement | - for loop - stop
for x in range(2, 10, 3):  # - for loop - start - increment - stop
    print(x)  # - log statement | - for loop - stop
x = 0  # - variable declaration |  while this isn't the start of the while loop, it is needed for the while loop to use as part of the conditional
while(x < 5):  # - while loop - start - stop
    print(x)  # - log statement
    x += 1  # - while loop - increment

pizza_toppings.pop()  # - Data Types - Composite - List - change value - delete value
# - Data Types - Composite - List - change value - delete value
pizza_toppings.pop(1)

print(person)  # - log statement
# - Data Types - Composite - Dictionary - access value - delete value
person.pop('eye_color')
print(person)  # - log statement

for topping in pizza_toppings:  # - Data Types - Composite - List - access value | - for loop - start - sequence
    if topping == 'Pepperoni':  # - conditional - if
        continue  # - for loop - continue
    print('After 1st if statement')  # - log statement
    if topping == 'Olives':  # - conditional - if
        break  # - for loop - break


def print_hello_ten_times():  # - function
    for num in range(10):  # - for loop - start - increment - stop
        print('Hello')  # - log statement


print_hello_ten_times()  # - function (call)


def print_hello_x_times(x):  # - function - parameter
    for num in range(x):  # - for loop - start - increment - stop
        print('Hello')  # - log statement


print_hello_x_times(4)  # - function (call) - argument


def print_hello_x_or_ten_times(x=10):  # - function - parameter - argument
    for num in range(x):  # - for loop - start - increment - stop
        print('Hello')  # - log statement


print_hello_x_or_ten_times()  # - function (call)
print_hello_x_or_ten_times(4)  # - function - argument


"""
Bonus section - comment - multiline
"""

# print(num3) # - log statement - comment - single line | - NameError: name <variable name> is not defined
# num3 = 72 # - comment - single line
# fruit[0] = 'cranberry' #- comment - single line | - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) #- comment - single line - log statement | - KeyError: 'favorite_team'
# print(pizza_toppings[7]) #- comment - single line - log statement | - IndexError: list index out of range
#   print(boolean) #- comment - single line - log statement | - IndentationError: unexpected indent
# fruit.append('raspberry') #- comment - single line | - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #- comment - single line | - AttributeError: 'tuple' object has no attribute 'pop'

""" 
cannot change, add, or delete with a Tuple
- Tuples
    - change value
    - add value
    - delete value
"""
