"""Ask for name and count number of vowels in name"""


def main():
    """Ask for users name, call functions and print"""
    name = input("What is your name? ")

    count = count_vowels(name)

    name_length = count_characters(name)

    print("Name:", name)
    print("Out of {} letters, {} has {} vowels.".format(name_length, name, count))


def count_vowels(name):
    """Count the number of vowels within the users input"""
    count = 0
    for letter in name:
        if letter.lower() in "aeiou":
            count += 1
    return count


def count_characters(name):
    """Remove the whitespace from the users name to give number of letters only"""

    # initial_length = name.split()
    # new_name = "".join(initial_length)
    # name_length = (len(new_name))
    # return name_length

    """Counts letters in users input instead of removing the white space - is simpler and therefore better"""

    name_length = 0
    for letter in name:
        if letter.isalpha():
            name_length += 1
    return name_length


main()
