import shelve

university = shelve.open('university_list')

# university['schedules'] = {
#     'monday_schedule': ['Math', 'English language', 'System programming', 'Python'],
#     'tuesday_schedule': ['English language', 'HTML', 'Python', 'Football'],
#     'wednesday_schedule': ['Physics', 'English language', 'Python'],
#     'thursday_schedule': ['Math', 'Chemistry', 'Java'],
#     'friday_schedule': ['Running', 'Math', 'Python', 'Math', 'Math'],
#     }
#
# university['tutors'] = {
#     'Math': ['Jack White', 'Jim Black'],
#     'Python': ['YouRa Allakhverdov', 'Jane Smith']
# }

print(university['schedules']['friday_schedule'])
print(university['tutors'])

university.close()
