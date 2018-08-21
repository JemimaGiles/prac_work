"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))

    get_score(score)
    print(get_score(score))


def get_score(score):
    if score < 0 > 100:
        return "invalid score"
    elif score > 90:
        return "excellent"
    elif score > 50:
        return "passable"
    else:
        return "bad"


main()
