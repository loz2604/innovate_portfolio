# # This process is known as casting
# # Is very useful when using input, because input's data type is always a string

# # Converting data types to integer
# print(int("54"))

# # When int is used on a float, it is always rounded down
# print(int(5.4))

# # If we want to round up or down according to the float, we need to use 
# print(int(round(5.9)))

# # This will convert to a floating point
# print(float(54))

# # Convert to a string (type) shows us what type of data we have
# print(type(str(54)))
# print(str(54))
# print(type(str(5.4)))
# print(str(5.4))

# # Truthy and Falsey

# print("What is your name?")
# name=input()

# if name:
#     print(f"Hello {name}")
# else:
#     print("You did not provide a name")

# # Not operator will flip the True/False statement

# # print(not True)
# # print(not False)

# bool = False
# if bool != True:
#     print(False)
# else:
#     print(True)

# # We can also write the same if statement in a different way

# bool = True
# if not bool:
#     print(False)
# else:
#     print(True)

# # Try/Accept - to catch errors without our code breaking
# # We could add exceptions to the except statement to specify specific errors
# #  For example ValueError will only pick up value errors

# def add_up():
#     num1 = input("Enter a number to add up  >   ")
#     num2 = input("Enter another number to add up   >   ")
#     try:
#         print(f"{num1} + {num2} is {int(num1) + int(num2)}")
#     except:
#         print("Error!")
#         print("*************")
#         add_up()

# add_up()

#  Global and Local scope

light = False

def light_switch():
    # The following line sets the scope og light
    global light    
    if light:
        print("Whoa! It's bright in here!")
        light = False
    else:
        print("Who turned out the lights?")
        light = True

light_switch()
light_switch()

balance = 100
def cash_withdrawal(amount):
    global balance
    print(f"Your balance is {balance}")
    print(f"You are withdrawing {amount}")
    balance -= amount
    print(f"Your balance is {balance}")

cash_withdrawal(20)
cash_withdrawal(10)
cash_withdrawal(5)

#  Lists and Tuples

list1 = [
    1,2,3
]

tuple1 = (
    1,2,3
)

coffee_order = [
    "Will - Black Americano",
    "Katy - Cappucino"
]

print(coffee_order[0])

# Change order
coffee_order[0] = "Will - Doppio Espresso"
print(coffee_order[0])

list_of_lists = [
[1,2,3],
[4,5,6]
]
print(list_of_lists[1][0])

# List - Can be changed
even_nums = [2,4,6,8,10]
# Tuple - Can't be changed
odd_nums= (1,3,5,7,9)
even_nums.append(12)

even_nums.insert(0, 0)

for i in even_nums:
    print(i)

# We can't do the following because the items are inside a tuple
# odd_nums.remove(1)
# odd_nums.pop()

# We can create a new tuple though

odd_nums += (11, 13, 15)
print(odd_nums)

# Slice notation

list_of_fruit = [
    "apples",
    "bananas",
    "oranges",
    "pears",
    "grapes",
    "pineapple",
    "starfruit",
    "mango",
    "cherries",
    "blackberries"
]
# Index positions, start:stop:step
print(list_of_fruit[1:7:2])

# 