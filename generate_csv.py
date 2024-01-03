import csv
import itertools

values = list()
for i in range(70):
    values.append(i + 1)

combinations = list(itertools.combinations(values, 5))

with open('data/megamil_allcomb.csv', 'w', newline='') as csvFile:
    csvWriter = csv.writer(csvFile, delimiter=' ')
    for i in range(len(combinations) - 1):
        csvWriter.writerow(combinations[i])