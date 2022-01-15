# Writing
colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

with open('D:/pythonDevelopFromZeroToPro/one_text.txt', 'w') as rainbow_colors:
    for colors in colors_list:
        print(colors, file=rainbow_colors)


# Append (Not Overwriting!)
colors_list_three = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

with open('D:/pythonDevelopFromZeroToPro/three_text.txt', 'a') as rainbow_colors_three:
    for colors in colors_list_three:
        print(colors, file=rainbow_colors_three)


# Reading
colors_list_two = []
with open('D:/pythonDevelopFromZeroToPro/one_text_01.txt', 'r') as rainbow_colors_two:
    for color in rainbow_colors_two:
        colors_list_two.append(color.strip('\n'))  # Method ".strip" will cut of choose characters from each element!

print(colors_list_two)
