from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, fuel, name, fanciness):
        super().__init__(fuel, name)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus flagfall of ${} = ${}".format(super().__str__(), self.flagfall, self.get_fare())

    def get_fare(self):
        return self.flagfall + super().get_fare()
