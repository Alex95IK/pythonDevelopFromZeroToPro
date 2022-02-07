import csv

with open('students1.csv', 'w', newline='') as file:
    headers_list = ['First name', 'Last name', 'Age']
    csv_writer = csv.DictWriter(file, fieldnames=headers_list)
    csv_writer.writeheader()
    csv_writer.writerow({
        'First name': 'Jack',
        'Last name': 'White',
        'Age': 24
    })
    csv_writer.writerow({
        'First name': 'Jane',
        'Last name': 'Black',
        'Age': 23
    })


# newline=''
# lineterminator='\n'
# encoding="utf-8"
