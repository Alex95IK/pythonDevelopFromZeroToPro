# unsort_list = [8, 2, 7, 3, 4, 5, 6, 2, 9, 3, 8, 7, 5, 3, 2, 6, 5, 8, 9, 6, 1, 5, 4, 7]

unsort_list = [8, 2, 7, 3, 4, 1, 5, 6, 2]


def stupid_sort(input_list):
    count = 0
    while True:
        if input_list[count] > input_list[count+1]:
            input_list.insert(count+1, input_list.pop(count))
            count = 0
        count += 1
        print(input_list)


stupid_sort(unsort_list)
