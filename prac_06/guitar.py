CURRENT_YEAR = 2018
VINTAGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def guitar_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.guitar_age() >= VINTAGE

    def __str__(self):
        # return ("{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost))
        return ("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, self.name, self.year, self.cost, VINTAGE))
