# #  Multiplication tables

# for x in range(1, 13):
#     for y in range(1, 13):
#         print(f"{x} x {y} =", x * y)
#     print("----------------------------------")

# start = int(input("please enter first number in multiplication table: "))
# end = int(input("please enter end number in multiplication table: "))
# print(f"multiplication table form {start} to {end}")
# for s in range(start, end + 1):
#     for e in range(start, end + 1):
#         print(f"{s} x {e} =", s * e)
#         print("-----------------------------------")

# # range game
# print("Between range game press [x] for exit!")

# while True:
#     number_1 = input("Enter first number: ")
#     if number_1 == "x":
#         break
#     number_2 = input("Enter second number: ")
#     if number_2 == "x":
#         break

#     elif number_1 < number_2:

#         for i in range(int(number_1)+1, int(number_2)):
#             print(i)

#     else:
#         print("number 1 should be less than number 2")


# number = int(input("Enter your number: "))

# if number < 20:
#     print("your number is less than 20.")
#     for i in range(number+1, 51):
#         print(i * 3)

# else:
#     print("your number is greater than 20.")
#     for i in range(number+1, 51):
#         print(i * 2)