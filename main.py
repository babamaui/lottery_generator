from gen_algorithm import *

# state = -1
# while state == -1:
#     print("\nLottery Number Generator\n\nSelect an option from below\n------")
#     print("[a] Mega Million")
#     print("[q] Quit Program")
#     print("------")
#     option = input("Input Option: ")
#     if option in ["a"]:
#         state = 1
#     elif option == "q":
#         state = 0
#     else:
#         print("Invalid Input - Try again\n")

# if state == 1:
#     validate_mega(generate_mega())

while True:
    sequence = generate_mega()
    if validate(sequence):
        break

print(sequence)