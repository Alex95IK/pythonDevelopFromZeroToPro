text = open('D:/pythonDevelopFromZeroToPro/sample.txt')

print(1, 2, 3, sep=':')
print(1, 2, 3, sep=':', end=' ')
print(1, 2, 3, sep=':', end='\n')  # \n - Is default parameter!


for line in text:
    print(line, end='')

text.close()  # Necessarily!!! We need close the file, which we are open!


# OPERATOR 'WITH' Automatic clothe the file!
with open('D:/pythonDevelopFromZeroToPro/sample.txt') as text:
    for line in text:
        print(line, end='')

with open('D:/pythonDevelopFromZeroToPro/sample.txt') as text:
    some_line = text.readline()
print(some_line)

with open('D:/pythonDevelopFromZeroToPro/sample.txt') as text:
    another_line = text.readlines()        # Method 'Readlines' read all are strings and paste them into the list!
print(another_line)

for one_line in another_line:
    print(one_line)
