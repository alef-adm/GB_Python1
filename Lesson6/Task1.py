import time


class TrafficLight:
    __color = "red"

    def running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        time.sleep(2)
        self.__color = "Green"
        return(self.__color)


a = TrafficLight()

print(a.running())
