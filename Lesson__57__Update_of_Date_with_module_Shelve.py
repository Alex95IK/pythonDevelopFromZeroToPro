import shelve

monday_schedule = ['Math', 'English language', 'System programming', 'Python']
tuesday_schedule = ['English language', 'HTML', 'Python', 'Football']
wednesday_schedule = ['Physics', 'English language', 'Python']
thursday_schedule = ['Math', 'Chemistry', 'Java']
friday_schedule = ['Running', 'Math', 'Python', 'Math', 'Math']


# with shelve.open('schedule', writeback=True) as sched:
with shelve.open('schedule') as sched:
    sched['monday'] = monday_schedule
    sched['tuesday'] = tuesday_schedule
    sched['wednesday'] = wednesday_schedule
    sched['thursday'] = thursday_schedule
    sched['friday'] = friday_schedule

    temp_list = sched['friday']
    temp_list.append('Swimming')
    sched['friday'] = temp_list

    # sched['friday'].append('Geography')

    for i in sched:
        print(i, sched[i])
