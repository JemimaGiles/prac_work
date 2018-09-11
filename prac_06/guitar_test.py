from prac_06.guitars import Guitars

CURRENT_YEAR = 2018


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    my_guitar = Guitars(name, year, cost)
    your_guitar = Guitars("a name", 2012, 1234)

    print(your_guitar.is_vintage())


main()
