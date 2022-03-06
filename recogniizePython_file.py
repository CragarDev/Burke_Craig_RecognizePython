num1 = 42  # - variable declaration - Data Types- Primitive- Numbers
num2 = 2.3  # - variable declaration - Data Types- Primitive- Numbers
boolean = True  # - variable declaration - Data Types- Primitive- Boolean
string = 'Hello World'  # - variable declaration - Data Types- Primitive- Strings
# - variable declaration - Data Types- Composite- List- initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}  # - variable declaration - Data Types - Primitive - Boolean - Numbers - Composite - List - initialize
fruit = ('blueberry', 'strawberry', 'banana')  # - variable declaration
print(type(fruit))  # - log statement - type check
print(pizza_toppings[1])  # - log statement
pizza_toppings.append('Mushrooms')
print(person['name'])  # - log statement
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

if num1 > 45:
    print("It's greater")  # - log statement
else:
    print("It's lower")  # - log statement

if len(string) < 5:  # - length check
    print("It's a short word!")  # - log statement
elif len(string) > 15:  # - length check
    print("It's a long word!")  # - log statement
else:
    print("Just right!")  # - log statement

for x in range(5):
    print(x)  # - log statement
for x in range(2, 5):
    print(x)  # - log statement
for x in range(2, 10, 3):
    print(x)  # - log statement
x = 0
while(x < 5):
    print(x)  # - log statement
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)  # - log statement
person.pop('eye_color')
print(person)  # - log statement

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')  # - log statement
    if topping == 'Olives':
        break


def print_hello_ten_times():
    for num in range(10):
        print('Hello')  # - log statement


print_hello_ten_times()


def print_hello_x_times(x):
    for num in range(x):
        print('Hello')  # - log statement


print_hello_x_times(4)


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')  # - log statement


print_hello_x_or_ten_times()  # - log statement
print_hello_x_or_ten_times(4)  # - log statement


"""
Bonus section - comment - multiline
"""

# print(num3) # - log statement - comment - single line
# num3 = 72 #- comment - single line
# fruit[0] = 'cranberry' #- comment - single line
# print(person['favorite_team']) #- comment - single line - log statement
# print(pizza_toppings[7]) #- comment - single line - log statement
#   print(boolean) #- comment - single line - log statement
# fruit.append('raspberry') #- comment - single line
# fruit.pop(1) #- comment - single line
