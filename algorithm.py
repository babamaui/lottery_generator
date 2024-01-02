import csv

def generate():
    return

with open('data/data_mini.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile)

    # Skip header line
    next(csvReader)

    for line in csvReader:
        print(line[1], line[2])