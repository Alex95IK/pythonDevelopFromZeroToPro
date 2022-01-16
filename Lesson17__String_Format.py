name = 'Jack'
age = 23

name_and_age = "My name is {}. I'm {} years old.".format(name, age)
# or
version02_name_and_age = "My name is {0}. I'm {1} years old.".format(name, age)
# or NEW VERSION, This is available only Python v. 3.6 or later
# Форматирование строковых ветераллов или f-strings
version03_name_and_age = f"My name is {name}. I'm {age} years old."

print(name_and_age)
print(version02_name_and_age)
print(version03_name_and_age)

# Also, we cen create KEYS for etch "Placeholder":
week_days = 'There are 7 days is a week: {mo} {tu} {we} {th} {fr} {sa} {su}.'\
    .format(mo='Monday', we='Wednesday', th='Thursday', tu='Tuesday', fr='Friday', su='Sunday', sa='Saturday')

print(week_days)

# We can set length limit to float, after for division operation
print('''
{0:10.3f} {1:10.3f} {2:10.3f}
{3:10.3f} {4:10.3f} {5:10.3f}
{6:10.3f} {7:10.3f} {8:10.3f}
'''. format(1.4888678754864, 2.48864648884454, 2.54834, 1.487276858970854, 7.8438556448494569496, 3.354, 5.58464856,
            8.6846848894, 3.546488449458))
