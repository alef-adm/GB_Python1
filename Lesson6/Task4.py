class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f'The car {self.name} went'
    def stop(self):
        return f'The car {self.name} stopped'
    def turn(self, direction):
        self.direction = direction
        return(f'The car {self.name} turn {direction}')
    def show_speed(self):
        return(f'The speed of this {self.color} {self.name} is {self.speed} km/h')

class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            return f'Warning!!! The speed of this {self.color} {self.name} is higher than 60 km/h!!!'
        else:
            return f'The speed of this {self.color} {self.name} is {self.speed} km/h'
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            return f'Warning!!! The speed of this {self.color} {self.name} is higher than 60 km/h!!!'
        else:
            return f'The speed of this {self.color} {self.name} is {self.speed} km/h'
class PoliceCar(Car):
    pass

lamba = SportCar(200, "Yellow", "Lamborghini", False)
volks = TownCar(50, "Blue", "Volkswagen", False)
ford = WorkCar(50, "Gray", "Ford", False)
print(lamba.turn("Right"))
print(lamba.show_speed())
print(volks.show_speed())
print(ford.show_speed())
