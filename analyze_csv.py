
import matplotlib.pyplot as plt
import csv
from gen_algorithm import validate

def mega_numspread():
    with open('data/megamil_full.csv', 'r') as csvfile_full:
        csvfile_full_reader = csv.reader(csvfile_full)

        # Skip header line
        next(csvfile_full_reader)

        index_0_list = list()
        index_1_list = list()
        index_2_list = list()
        index_3_list = list()
        index_4_list = list()
        index_5_list = list()

        for line in csvfile_full_reader:
            sequence = [int(i) for i in line[1].split()]

            index_0_list.append(sequence[0])
            index_1_list.append(sequence[1])
            index_2_list.append(sequence[2])
            index_3_list.append(sequence[3])
            index_4_list.append(sequence[4])

            index_5_list.append(int(line[2]))

    figure, axis = plt.subplots(2, 3, figsize=(12, 8))

    # Index 0
    axis[0, 0].hist(index_0_list, 70, (1, 70), color = 'green', histtype = 'bar', rwidth = 1)
    axis[0, 0].set_title("Index 0")

    # Index 1
    axis[0, 1].hist(index_1_list, 70, (1, 70), color = 'green', histtype = 'bar', rwidth = 1)
    axis[0, 1].set_title("Index 1")

    # Index 2
    axis[0, 2].hist(index_2_list, 70, (1, 70), color = 'green', histtype = 'bar', rwidth = 1)
    axis[0, 2].set_title("Index 2")

    # Index 3
    axis[1, 0].hist(index_3_list, 70, (1, 70), color = 'green', histtype = 'bar', rwidth = 1)
    axis[1, 0].set_title("Index 3")

    # Index 4
    axis[1, 1].hist(index_4_list, 70, (1, 70), color = 'green', histtype = 'bar', rwidth = 1)
    axis[1, 1].set_title("Index 4")

    # Index 5
    axis[1, 2].hist(index_5_list, 25, (1, 25), color = 'gold', histtype = 'bar', rwidth = 1)
    axis[1, 2].set_title("Index 5")

    plt.show()

def main():
    mega_numspread()
    
main()