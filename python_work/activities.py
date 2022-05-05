#  Activity 1

# string = "Welcome to Code Nation!"
# length = len(string)
# print(length)

# def string_check():
#     if length % 2 == 0:
#         print(f"The string, {string} Is {length} characters in length. It is an even number")
#     else:
#         print(f"The string, {string} Is {length} characters in length. It is an odd number")

# string_check()

#  Activity 2

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in alphabet:
    print(i)

def check_letter():
    alphabet_index = int(input("Please enter a number between 1 & 26    >   "))
    if alphabet_index >= 1 and alphabet_index <= 26:
        alphabet_index -= 1
        print("The letter that corresponds with that number is " + alphabet[alphabet_index])
    else:
        check_letter()

check_letter()

# Activity 3

# pos1 = 1
# pos2 = 2
# pos3 = 3
# pos4 = 4
# pos5 = 5
# pos6 = 6
# pos7 = 7
# pos8 = 8
# pos9 = 9


# def start_game():
#     player = input("Please choose x or o    >   ")
#     if player.lower() == "x" or player.lower() == "o":
#         print(f"You have chosen {player}")
#         if player == "x":
#             computer = "o"
#             print(f"Computer is {computer}")
#         elif player == "o":
#             computer = "x"
#             print(f"Computer is {computer}")
#         print_board()
        
#         choose_place()
#     else:
#         start_game()

# def print_board():
#     print("       |       |       ")
#     print(f"   {pos1}   |   {pos2}   |   {pos3}   ")
#     print("_______|_______|_______")
#     print("       |       |       ")
#     print(f"   {pos4}   |   {pos5}   |   {pos6}   ")
#     print("_______|_______|_______")
#     print("       |       |       ")
#     print(f"   {pos7}   |   {pos8}   |   {pos9}   ")
#     print("       |       |       ")

# def choose_place():
#     choice = int(input("Please choose a number that corresponds with the place on the board you want to play    >   "))
#     if choice >=1 and choice <=9: 
#         print(f"You have chosen {choice}")
#     else:
#         choose_place()
#     if choice == 1:
#         pos1 = player
#         print("       |       |       ")
#         print(f"   {pos1}   |   {pos2}   |   {pos3}   ")
#         print("_______|_______|_______")
#         print("       |       |       ")
#         print(f"   {pos4}   |   {pos5}   |   {pos6}   ")
#         print("_______|_______|_______")
#         print("       |       |       ")
#         print(f"   {pos7}   |   {pos8}   |   {pos9}   ")
#         print("       |       |       ")
#         print("Computer's Turn...")

# start_game()