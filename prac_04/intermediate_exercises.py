def main():
    numbers = []
    count = 0

    get_numbers(count, numbers)

    list_length = (len(numbers))
    list_minimum = (min(numbers))
    list_maximum = (max(numbers))
    list_average = (sum(numbers) / len(numbers))

    print_funfacts(list_average, list_maximum, list_minimum, numbers, list_length)


def print_funfacts(list_average, list_maximum, list_minimum, numbers, list_length):
    print("The length of the list is {}".format(list_length))
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(list_minimum))
    print("The largest number is {}".format(list_maximum))
    print("The average of the numbers is {}".format(list_average))


def get_numbers(count, numbers):
    while count != 5:
        get_number = int(input("please enter a number "))
        count = count + 1
        numbers.append(get_number)


main()
