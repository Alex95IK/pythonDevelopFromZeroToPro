text = 'Hello Python!'
print(text[3])

print('Hello Python!'[3])

print(text[:2])
print(text[:2:1])

# Incorrect!:
new_text = text[8:10]
print('Pa' + new_text)

# Correct!:
print('Hello Python!'[6:7] + 'a' + 'Hello Python!'[8:10])