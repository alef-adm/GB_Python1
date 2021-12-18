class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if (self.num -other.num) > 0:
            return Cell(self.num - other.num)
        else:
            print("Вычитание невозможно")

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, param):
        return (('*' * param) + '\n') * (self.num //param) + '*' * (self.num % param)



c1 = Cell(5)
c2 = Cell(13)
print(c2.make_order(5))