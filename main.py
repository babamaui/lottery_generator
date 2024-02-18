from gen_algorithm import *

while True:
    sequence = generate_mega()
    if validate(sequence):
        break

print(sequence)