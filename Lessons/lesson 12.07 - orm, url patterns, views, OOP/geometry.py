class Point:

    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    x = property(get_x, set_x)

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    y = property(get_y, set_y)

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    color = property(get_color, set_color)

    def get_info(self):
        return f"{self.color} point ({self.x},{self.y})"

    info = property(get_info)

    def __str__(self):
        return self.info


p = Point(2,4,"red")
print(p.info)
print(p)



    