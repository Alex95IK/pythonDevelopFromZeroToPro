# Module Pickle
import pickle

honda = (
    'civic',
    'gray',
    '2009',
    (
        (1, 'James Brown'),
        (2, 'Jane White'),
        (3, 'Jake Green'),
    )
)

with open('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)


with open('honda.pickle', 'rb') as honda_retrieved:
    car_one = pickle.load(honda_retrieved)

print(car_one)


# Append (Overwriting)
# Append (Overwriting)
models = ['civic', 'accord', 'pilot']
owners = ['James Brown', 'Jane White', 'Jake Green']

with open('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)
    pickle.dump(models, honda_file)
    pickle.dump(owners, honda_file)
    pickle.dump(127827, honda_file)

with open('honda.pickle', 'rb') as honda_file_two:
    car_two = pickle.load(honda_file_two)
    car_models = pickle.load(honda_file_two)
    car_owners = pickle.load(honda_file_two)
    some_num = pickle.load(honda_file_two)

print(car_two)
print(car_models)
print(car_owners)
print(some_num)
