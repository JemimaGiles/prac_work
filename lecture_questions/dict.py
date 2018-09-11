names_to_ages = {"bill": 21, "jane": 4, "jack": 56}


name = input("what is your name? ")
age = input("what is your age? ")

names_to_ages[name] = age

print(names_to_ages)

print("Name: {}".format(name))
print("Age: {}".format(age))

for name, age in names_to_ages.items():
    print(name, '-', age)
