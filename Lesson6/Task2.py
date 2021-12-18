class Road:
    def __init__(self, l1, width, thickness):
        self.__length = l1
        self.__width = width
        self.thickness = thickness

    def calculate(self):
        return int(self.__length) * int(self.__width) * 25 * int(self.thickness)


my_road = Road(200, 50, 10)
print(my_road.calculate())

