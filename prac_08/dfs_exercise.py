from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.SilverServiceTaxi import SilverServiceTaxi

MENU = "(Q)uit, (C)hoose, (D)rive"


def main():
    total_bill = 0
    taxis = [Taxi(100, "Prius"), SilverServiceTaxi(200, "Aston Martin", 5), SilverServiceTaxi(100, "Hummer", 3)]

    print("let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == 'd':
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${}".format(current_taxi.name, trip_cost))

            total_bill += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${}".format(total_bill))
    print("Taxis are now: ")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))


main()
