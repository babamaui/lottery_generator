import csv
import random
from datetime import datetime

# Invalidates sequences that have specified patterns/in winning list
# Formerly called remove()
def validate(sequence):
        #
        # Remove if there are linear increment patterns (ex. 1, 2, 20, 40, 41)
        increments = list()
        for i in range(len(sequence) - 1):
            increments.append(sequence[i+1] - sequence[i])
        
        # Get the increment delta (ex. 1, 18, 20, 1) so when set is made there is a duplicate
        if len(increments) - len(set(increments)) > 1:
            return False
        
        #
        # Remove if all even/odd
        even_odd = list(i % 2 for i in sequence)
        if len(set(even_odd)) == 1:
            return False
        
        return True

# Generate a sequence for the Mega Millions lottery
    # Indices 0-4 are positive numbers 1 - 70 (inclusive)
    # Index 5 is a positive number 1 - 25 (inclusive)
def generate_mega():
    # Set seed based on current time
    random.seed(datetime.now().timestamp())

    sequence = list()
    min = 1
    max = 70

    # Generate the first 5 numbers
    for i in range(5):
        if i == 0:
            current = random.randint(1, 46)
        elif i == 1:
            current = random.randint(min, 63)
        elif i == 2:
            current = random.randint(min, 68)
        elif i == 3:
            current = random.randint(min, max - 1)
        elif i == 4:
            current = random.randint(min, max)
        sequence.append(current)
        min = current + 1

    # Generate index 5 Mega Ball
    sequence.append(random.randint(1, 25))

    return sequence

def validate_mega(sequence):
    # Remove if the normal digits are part of the past winning sequences
    with open('data/megamil_sample.csv', 'r') as csvfile_sample:
        csvfile_sample_reader = csv.reader(csvfile_sample)

        # Skip header line
        next(csvfile_sample_reader)

        # Check sequence against past winning sequences
        for line in csvfile_sample_reader:
            past_sequence = [int(i) for i in line[1].split()]
            
            # If the regular numbers are the same, return false (excluding the Mega Ball at index 5)
            if past_sequence == sequence:
                return False
    
    return validate(sequence)

# def analyze_mega():
#     # Run remove on all combinations
#     with open('data/megamil_allcomb.csv', 'r') as csvfile_allcomb:
#         csvfile_allcomb_reader = csv.reader(csvfile_allcomb)

#         # Skip header line
#         next(csvfile_allcomb_reader)

#         # Track number of winning sequences that would pass through the validation algorithm
#         total_count = 0
#         valid_count = 0

#         for line in csvfile_allcomb_reader:
#             past_sequence = [int(i) for i in line[0].split()]
#             if remove(past_sequence):
#                 valid_count += 1
#             total_count += 1

#         print("All Combination Stats:")
#         print(valid_count, "/", total_count, "sequences marked as valid by algorithm")
#         print(round((valid_count/total_count)*100, 3), "% of sequences valid")

#     # Run remove on only winning numbers
#     with open('data/megamil_full.csv', 'r') as csvfile_win:
#         csvfile_win_reader = csv.reader(csvfile_win)

#         next(csvfile_win_reader)

#         # Track number of winning sequences that would pass through the validation algorithm
#         total_count = 0
#         valid_count = 0

#         for line in csvfile_win_reader:
#             past_sequence = [int(i) for i in line[1].split()]
#             if remove(past_sequence):
#                 valid_count += 1
#             total_count += 1

#         print("\nWinning Sequence Stats:")
#         print(valid_count, "/", total_count, "sequences marked as valid by algorithm")
#         print(round((valid_count/total_count)*100, 3), "% of sequences valid")