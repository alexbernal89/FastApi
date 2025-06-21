# Going to deploy print Python
"""
welcome = 'Welcome to Python'
welcome1 = "Welcome to Python1"
print(welcome)
print(welcome1)
"""
'''
Espacio
'''

#Ejercicio
"""
balance = 50
item = 15
tax = 0.03
value = item * (1+tax)
final_balance = balance - value
print(value)
print(final_balance)

#Formatear variables
first_name = "Alex"
last_name = "Bernal"
print(f"Hi {first_name}")
sentence = "Hi {} {}"
print(sentence.format(first_name, last_name))
print(f"Hi {first_name} {last_name} welcome")
"""
#Input
"""first_name = input("What is your name:")
days =  int(input('How many days before yuu birthday:'))
weeks = round(days/7,2)
print(f"Hello {first_name}, "
      f"only {weeks} weeks before your birthday")
"""
# List
"""
My_List = [80, 90, 'hello', "hello", 50, 60]
print(My_List)
My_List.append(1000)
print(My_List)
My_List.insert(2,300)
print(My_List)
My_List.remove(60)
print(My_List)
My_List.pop(0)
print(My_List)

#My_List.sort()
print(My_List)
"""
# Sets, they are similar to lists but they are ordered and can't contain duplications, it uses curly brackets
"""My_set = {8,1, 2, 3, 4, 5, 6, 9, 1, 3}
print(My_set)
print(len(My_set))
for x in My_set:
        print(x)

My_set.discard(8)
print(My_set)
My_set.clear()
print(My_set)
My_set.add(10)
print(My_set)
My_set.update([11,12])
print(My_set)"""

#Tuples, they are ordered like a lists, but they are unchangeable and we use parentheses
# We use this when the information don't change
"""My_tuple = (1, 2, 3, 4, 5, 3, 5)
print(My_tuple)
print(len(My_tuple))"""

#Excersise
"""
Zoo = ["lion", "chicken", "duck", "cat", "dog"]
print(Zoo)
Zoo.pop(2)
print(Zoo)
Zoo.append('bird')
print(Zoo)
print(Zoo[0:3])
"""
# Booleans an Operators
"""
like_pizza = True
like_hamburguer = False
print(type(like_pizza))
print(type(like_hamburguer))
#Comparasition operators
print(1==2)
print(1!=2)
print(1>2)
print(1<2)
print(1>=1)
print(1<=2)

# Logical Operators
print(1>3 and 5<7)
print(1>3 or 5<7)
print(1==1)
print(not(1==1))
print(not(1==2))
"""
#Flow control - if else elifx
"""
x=1
if x > 2:
    print("x is greater than 1")
else:
    print("x isn't greater than 1")

print("Outside the statement")
"""
"""
hour = 19
if hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
else:
    print("Good night!")
"""
"""
grade = 80
if grade >= 90:
    print("A")
elif 80<= grade <90:
    print("B")
elif 70<= grade <80:
    print("C")
elif 60<= grade <70:
    print("D")
else :
    print("F")
"""
#For and While loops
# For we can specify range o numbers
# while continue iterator until a condition is met
"""
my_list=[1,2,3,4,6]
for iterator in my_list:
    print(iterator)

for x in range(3,10):
    print(x)
added = 0

for x in my_list:
    added += x
print(added)
"""
""""""
"""
week = ['monday', 'tuesday', 'wenesday', 'thursday', 'friday']
for x in week:
    print(f"happy {x} !")
""""""
i=0
while i<5:
    i +=1
    if i == 3:
        continue
    print(i)
    if i ==4:
        break

else:
    print('i is no larger than five')
#while x in week:
#  print(f"happy {x} !")
"""
"""
Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

- Create a while loop that prints all elements of the my_list variable 3 times.

- When printing the elements, use a for loop to print the elements

- However, if the element of the for loop is equal to Monday, continue without printing
# Solution 1
i=0
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
while i < 3:
    for x in my_list:
        if x != "Monday":
            print(f"{x}")
    i+=1
# Solution 2
i=0
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
while i < 3:
    i= i+1
    for x in my_list:
        if x == "Monday":
            print("----------")
        print(x)
"""
"""
# Dictionaries (key and value)
user_dictionary = {
    'username': 'Alex',
    'name':'Alex Bernal',
    'age': 32
}
user_dictionary['Married']=True
print(len(user_dictionary))
print(user_dictionary.get('username'))
user_dictionary.pop('age')
print(user_dictionary)
#user_dictionary.clear()
#print(user_dictionary)
#del user_dictionary

# Print la clave valor
for x,y in user_dictionary.items():
    print(x,y)
#Copia del diccionario
user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop('name')
print(user_dictionary)
# Gestión de memoria borra los dos la copia y original
user_dictionary2 = user_dictionary
user_dictionary2.pop('name')
print(user_dictionary)
"""
# Exercise
"""
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
for x,y in my_vehicle.items():
    print(x,y)
my_vehicle2=my_vehicle.copy()
print(my_vehicle2)
my_vehicle2['number_of_tires']=4
print(my_vehicle2)
my_vehicle2.pop('mileage')
print(my_vehicle2)
for x in my_vehicle2:
    print(x)
"""
# functions
"""
def my_function():
    print('Alex inside')

my_function()

def print_my_name(first_name, last_name):
    print(f"my naame is {first_name} {last_name}")

print_my_name('Alex', 'Bernal')

"""

# Variables internas y externas

"""def print_color():
    color= 'red'
    print(color)
color= 'blue'
print(color)
print_color()
"""
"""
#Orden de parametros
def numbers(highest, lowest):
    print(highest)
    print(lowest)

numbers(10, 3)
numbers(lowest=10, highest=3)
"""
#Multiplicaciones
"""
def multiply_numbers(a,b):
    return a * b
result=multiply_numbers(2,3)
print(result)
# List
def print_list(list):
    for x in list:
        print(x)

my_list=[1, 2, 3, 4, 5, 6]
print_list(my_list)
"""
'''
#Funciones que llama a otra función
def cost_item(cost):
    return cost + tax_item(cost)

def tax_item(cost):
    tax=0.19
    return cost * tax
final_price=cost_item(100)
print(final_price)
'''
def parameters(firstname, lastname, age):
    dictionary = {
        'firstname':firstname,
        'lastname': lastname,
        'age': age
    }
    for x,y in dictionary.items():
        print(x,y)
    return dictionary

dictionary2 = parameters('Alex', 'bernal', 30)

print(dictionary2)