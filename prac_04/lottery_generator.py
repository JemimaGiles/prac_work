import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    quick_pick_amount = int(input("how many quick picks do you want? "))
    while quick_pick_amount < 0:
        print("pick a number greater than 0")
        quick_pick_amount = int(input("how many quick picks do you want? "))

    for i in range(quick_pick_amount):
        quick_picks = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_picks:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_picks.append(number)
        quick_picks.sort()

        print(" ".join("{:2}".format(number) for number in quick_picks))


main()
