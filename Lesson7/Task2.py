

class Clothes:
    def __init__(self, s):
        self.s = s


class Coat(Clothes):
    @property
    def coat_calculate(self):
        cloth = int(self.s)*6.5 + 0.5
        return cloth

class Costume(Clothes):
    @property
    def costume_calculate(self):
        cloth = 2 * int(self.s) + 0.3
        return cloth


coat = Coat(56)
print(coat.coat_calculate)
costume = Costume(180)
print(costume.costume_calculate)