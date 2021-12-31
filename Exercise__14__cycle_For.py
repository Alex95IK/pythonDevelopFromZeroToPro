# Ex 01
x = 0

for count in range(10, 31):
    if count % 2 == 0:
        x += count

print(x)

# Ex 02
user_number = int(input('Please enter the number'))

for _ in range(user_number):
    print('Hello!')
