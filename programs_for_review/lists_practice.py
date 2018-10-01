"""Ask users for and add users score to list and display maximum score"""


def main():
    """Contain the list and run functions"""
    scores = []

    add_score = True

    menu_choices(add_score, scores)

    highest_score = maximum_score(scores)
    print("You highest score was: {}".format(highest_score))


def menu_choices(add_score, scores):
    """Ask to add scores or view highests score. Error check """
    while add_score:
        try:
            menu = int(input("1.Enter score\n2.See scores\n"))
            if menu == 1:
                enter_valid_input(scores)
            elif menu == 2:
                add_score = False
                maximum_score(scores)
            else:
                print("Enter either 1 or 2")
                menu = int(input("1.Enter score\n2.See scores\n"))
        except ValueError:
            print("Enter either 1 or 2")


def maximum_score(scores):
    """Find highest number in list"""
    highest_score = 0
    for number in scores:
        if number > highest_score:
            highest_score = number
    return highest_score


def enter_valid_input(scores):
    """Error check the users entered score"""
    valid_input = False
    while not valid_input:
        try:
            score = int(input("Score: "))
            if score < 0:
                print("Invalid score, must non negative")
            else:
                scores.append(score)
                valid_input = True
        except ValueError:
            print("This is not a number")
    return scores


main()
