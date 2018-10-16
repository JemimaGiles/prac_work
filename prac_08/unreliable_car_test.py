from prac_08.unreliable_car import UnreliableCar


def main():
    new_car = UnreliableCar(100, "Reliable", 90)
    old_car = UnreliableCar(100, "Unreliable", 9)

    for i in range(1, 12):
        print("Attempting to drive car {}km".format(i))
        print("{} drove {}km".format(new_car.name, new_car.drive(i)))
        print("{} drove {}km".format(old_car.name, old_car.drive(i)))

    print(new_car)
    print(old_car)


main()
