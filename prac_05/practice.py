names = {}

count = 0
while count != 5:
    count = count + 1
    name = input("please enter a name: ").title()
    date_of_birth = list(input("please enter their date of birth in **/**/**** format: ").split('/'))
    age = int(date_of_birth.pop(2))
    dob = (2018 - age)

    names[name] = dob

max_length = max(len(name) for name in names)
for name, age in names.items():
    print("{:{}} : {}".format(name, max_length, age))
