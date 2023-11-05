# import random

# top_of_range = input("Type a number: ")

# if top_of_range.isdigit:
#     top_of_range = int(top_of_range)

#     if top_of_range <= 0:
#         print("Please type a number larger than 0 next time. ")
#         quit()
# else:
#     print('Please type a number next time. ')
#     quit()

# number_random = random.randint(0, top_of_range)
# guesses = 0

# while True:
#     guesses += 1
#     user_guess = input("make a guess: ")
#     if user_guess.isdigit:
#         user_guess = int(user_guess)
#     else:
#         print("Please type a number next time. ")
#         continue

#     if user_guess == number_random:
#         print("You got it!")
#         break
#     elif user_guess > number_random:
#         print("You were above a number!")
#     else:
#         print("You were below a number!")

# print("You got it in", guesses, "guesses" )
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

print(CLEAR)

num1 = input(f"{CLEAR_AND_RETURN} Enter the first number: \n")

