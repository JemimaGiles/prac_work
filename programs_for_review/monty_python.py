"""Monty Python insult generator - Grammar not included"""
import random


def main():
    run_away = False

    while not run_away:
        subjects = ["Your face", "Your mother", "Your Father", "Your horse"]
        descriptions = ['smells', 'looks', 'sounds', 'has a brain']
        nouns = ['hamster', 'elderberry', 'window dresser', 'silly-person', 'pig-dog', 'duck']

        subject_index = random.choice(subjects)
        description_index = random.choice(descriptions)
        noun_index = random.choice(nouns)

        print("{} {} of {}\n".format(subject_index, description_index, noun_index))

        print("Now go away or I will taunt you a second time!\n")

        print("What do you want to do?\n")
        print("1. Run Away!!")
        print("2. I demand entrance to this sacred castle")

        choice = int(input(""))

        if choice == 1:
            run_away = True
            print("And now remain gone you daffy english knights!")
            return run_away


main()
