CURRENT_YEAR = 2018
VINTAGE = 50


class Guitars:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def guitar_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.guitar_age() >= VINTAGE

    def __str__(self):
        return ("{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost))
