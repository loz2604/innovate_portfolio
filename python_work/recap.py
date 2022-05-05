
import random


print("this is my current file")
# This is how we comment in python
# Or use ctrl / to comment blocks of code

# Variables
greeting = "Hello World!"
print(greeting)

# strings are for representing characters
print("Hello my name is Loz")
print("1234")

# Integer - whole number
print(1234)

# Floating point - any number with a decimal point
print(12.34)

# Boolean - true/false Needs a capital letter
print(True)
print(False)

# None - Null, or blank
print(None)

# Strings have methods that we can use to manipulate them and properties which are essentially just information.

# Prints the number of characters in the string
print(len("hello"))

# Prints the second character of the string (index position[1])
print("hello"[1])

# Target the last character of the string
print("hello"[-1])

# Dot Notation is a way of accessing methods
print(greeting.upper())

# Other methods that we can use are
#.lower()
# .capitalize()
# .count()
# .find()
# .replace()
# .strip()

# Libraries

#  eg import random - always do this right at the top of the page
#  generates a random number between o and 1 (doesn't include 1) is a floating point
print(random.random())
# generates a random number between 1 and 10 (inclusive), is a floating point
print(random.uniform(1,10))
#  generates a random number between 1 and 10 (inclusive), is a whole number
print(random.randint(1,10))

#  Can import methods in different ways too
from random import random,randint,uniform
#  Using this method we don't need to use dot notation, we just use the method we want to use
print(randint(1,100))

#  Variables

# remember we use snake_case

my_name = "Loz"
my_age = 43

print(my_name,my_age)

print("Hi my name is", my_name)
#  concatenation only attaches strings to strings
print("Hi, I am " + my_name)
# We can use dot format to attach strings and integers
print("Hello, I am called {} and I am {} years old".format(my_name,my_age))
# We can use an f string
print(f"Hello, my name is {my_name} and I am {my_age} years old")

# Assignment operator (=)
# Arithmetic Operators for calculations

# + - addition
# - - minus
# * - multiplication
# ** - to the power of
# / - division
# % - modulus

print(1+2)
print(1-2)
print(2*3)
print(2**3)
print(15/3)
print(15%3)

balance = 100
amount = 50

print(balance-amount)
balance = balance - amount
#  or
balance -= amount
print(balance)

# Inputting information

char_name = input("What is your name?   >   ")

print(f"Welcome, {char_name}")

# if/elif/else
# Comparison Operators

music = "ska"

if music == "classical":
    print("Oh no not classical music again!")
elif music == "pop":
    print("Really? POP?!")
else:
    print("This is more like it!")

# The following will print true
print(10%2==0)

# Other comparison operators

# >= - greater than or eqaul to
# <= - less than or equal to
# > - greater than
# < - less than

num1 = 60
num2 = 30

if num1<num2:
    print("number 2 is bigger than number 1")
elif num1 > num2:
    print("number 1 is bigger than number 2")
else:
    print("Both numbers are the same size")

# Assignment operators

num = 21

if num%7==0 and num%3==0:
    print("fizzbuzz") 
elif num%3==0:
    print("fizz")
elif num%7==0:
    print("buzz")
else:
    print(num)

# Logical Operator. AND Both sides of the and need to be true for the whole thing needs to be true

place = "MCR"
weather = "cloudy"

if place == "MCR" and weather == "sunny":
    print("check again!")
elif place == "MCR" and weather =="rain":
    print("Obvs")
else:
    print("Wait, it isn't raining?!")

#  Logical operator OR either side of OR can be true for the whole thing to be true

day = "Tuesday"
bank_holiday = False

if day == "Saturday" or day == "Sunday" or bank_holiday == True:
    print("Yay, it's a day off")
else:
    print("I am off to code nation")

#  Functions

def light_switch():
    print("Who turned out the lights?!")

light_switch()

def cash_withdrawal (amount, accnum):
    print(f"Withdrawing {amount} from account {accnum}")

cash_withdrawal(300, 4321234)
cash_withdrawal(200, 1234566)
cash_withdrawal(100, 7247903)
cash_withdrawal(500, 1205287)

# All functions want to return to their caller.
#  If we want to do more with the result of the function, we use return inside the function, this allows us to do more with the result of the function outside of the function

def add_up(num1,num2):
    return num1+num2

print(add_up(5,3))

# Lists (always use [])

coffee_order = [
    "Alex -Cortado",
    "Ben - Latte",
    "Charlie - Whatever's new"
]

# We can print the item in a list by it's index
print(coffee_order[1])

# Can use index to update or change a list
coffee_order[2]="Loz - Americano"

print(coffee_order)

# Adds to the end of the list
coffee_order.append("Charlie - Whatever's new")
print(coffee_order)

# Removes an item from the list
# If we include an integer, it will delete from the list at that index
# If we don't enter a parameter, the last thing on the list will be deleted
coffee_order.pop()
coffee_order.pop(1)

# For loops

fav_drinks = ["coke", "fanta", "lemonade"]

for i in fav_drinks:
    print(i)

for i in range(10):
    print(i)

#  Range can take 3 parameters - called slice notation, start, stop, step
for i in range(2,12,2):
    print(i)

#  While loops
# Remember the order in which you place the instructions within the while loop matters
# Why do these two functions produce different results? 

number = 0
while number < 10:
    print(number)
    number += 1

number2 = 0
while number2 < 10:
    number2 += 1
    print(number2)