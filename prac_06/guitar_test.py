from prac_06.guitar import Guitar

CURRENT_YEAR = 2018


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    my_guitar = Guitar(name, year, cost)
    your_guitar = Guitar("a name", 2012, 1234)

    print(my_guitar)


main()
