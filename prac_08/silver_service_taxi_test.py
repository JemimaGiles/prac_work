from prac_08.SilverServiceTaxi import SilverServiceTaxi


def main():
    aston_martin = SilverServiceTaxi(100, '007', 5)
    porsche = SilverServiceTaxi(100, "Porscha", 3)
    honda = SilverServiceTaxi(100, "Lucy", 2)

    aston_martin.drive(30)
    porsche.drive(20)
    honda.drive(18)

    print(aston_martin)
    print(porsche)
    print(honda)


main()
