import csv


def add_student(first_name, last_name, age):
    with open('students.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow([first_name, last_name, age])
        file.close()


add_student('Jon', 'Snow', 196)
