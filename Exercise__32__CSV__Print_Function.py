import csv


def print_students(file_csv):
    with open(file_csv, newline='') as file:
        csv_reader = csv.reader(file)
        for i in csv_reader:
            print(i)


print_students('students.csv')
