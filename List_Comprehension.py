
some_string = 'Hello'

some_list = [ll+'=' for ll in some_string]
print(some_list)

sd = [i ** 2 for i in range(0, 16) if i % 2]

print(sd)

sl = ['+' if i % 2 else '-' for i in range(0, 16)]

print(sl)
