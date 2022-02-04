import csv


with open('cars1.csv') as file:
    csv_reader = csv.reader(file, delimiter=";")
    next(csv_reader)
    for car in csv_reader:
        print(f'{car[1]} {car[2]} cost {car[3]} m')


with open('cars1.csv') as file:
    csv_reader = csv.DictReader(file, delimiter=";")
    for car in csv_reader:
        print(f'{car["Year"]} {car["Model"]} cost {car["Length"]} m')

