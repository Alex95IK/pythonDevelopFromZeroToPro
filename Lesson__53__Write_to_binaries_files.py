# Write to binaries files
with open('test_binary', 'bw') as test_file:
    for number in range(21):
        test_file.write(bytes([number]))

with open('test_binary', 'br') as test_file:
    for number in test_file:
        print(number)


with open('test_binary_two', 'wb') as test_file_two:
    test_file_two.write(bytes(range(15)))

with open('test_binary_two', 'rb') as test_file_two:
    for number in test_file_two:
        print(number)
