"""Testing the taxi class which has inherited its data from the car class"""

from prac_08.taxi import Taxi


def main():
    my_taxi = Taxi('', '', 1.23)
    my_taxi.name = 'Prius 1'
    my_taxi.fuel = 100
    my_taxi.drive(40)

    print(my_taxi)
    print('Fare: ${}'.format(my_taxi.get_fare()))

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print('Fare: ${}'.format(my_taxi.get_fare()))


main()
