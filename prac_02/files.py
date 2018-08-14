OUTPUT_FILE = "name.txt"
INPUT_FILE = "name.txt"
INPUT_NUMBERS_FILE = "numbers.txt"

out_file = open(OUTPUT_FILE, 'w')
user_name = input("What is your name? ")
print(user_name, file=out_file)
out_file.close()

in_file = open(INPUT_FILE, 'r')
user_name = in_file.read()
print("your name is: {}".format(user_name))
in_file.close()

in_file = open(INPUT_NUMBERS_FILE, 'r')
# readlines makes it read the individual lines, gets rid of /n problem
total = 0
for line in in_file:
    # line is a thing
    number = int(line)
    total = total + number
print(total)

in_file.close()
