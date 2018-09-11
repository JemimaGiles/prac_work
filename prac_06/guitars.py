from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My Guitars!")
    # name = input("Name: ")
    # year = int(input("Year: "))
    # cost = int(input("Cost: "))
    # guitar = Guitar(name, year, cost)
    # guitars.append(guitar)

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print(guitars)


main()
