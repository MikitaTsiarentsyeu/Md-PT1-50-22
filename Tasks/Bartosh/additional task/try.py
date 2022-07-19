class Engine:

    def __init__(self, power, volume):
        self.__power = power 
        self.__volume = volume

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    power = property(get_power, set_power)

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        self.__volume = volume

    volume = property (get_volume, set_volume)

en = Engine(100, 6)
    
print (en.power)

class SuperCar:

    def __init__(self, make, model, power, volume):
        self.__make = make 
        self.__model = model
        self.__engine = Engine(power, volume)

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    make = property (get_make, set_make)

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    model = property (get_model, set_model)

    def get_engine(self):
        return self.__engine

    def set_engine(self, power, volume):
        self.__engine = Engine(power, volume)

    engine = property (get_engine, set_engine)
   

sc = SuperCar("Rarri", "LaRarri", 1000, 6)

print (sc.make)
print (sc.model)
print (sc.engine.power)
print (sc.engine.volume)