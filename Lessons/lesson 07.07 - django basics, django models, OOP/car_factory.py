class Engine:

    def __init__(self, power, volume):
        self.__power = power
        self.__volume = volume

    def get_power(self):
        return self.__power

    def get_volume(self):
        return self.__volume


class SuperCar:

    def __init__(self, make, model, power, volume):
        self.__make = make
        self.__model = model
        self.__engine = Engine(power, volume)

class MehCar:

    def __init__(self, make, model, engine):
        self.__make = make
        self.__model = model
        self.__engine = engine

sc = SuperCar("Ferrari", "la Ferrari", 1000, 6.5)

engine = Engine(150, 1.5)
mc = MehCar("Lada", "Granta", engine)