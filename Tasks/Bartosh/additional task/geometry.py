class Point:
    def __init__(self, x , y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
          
    def set_x(self, x):
        self.__x = x

    x = property (get_x, set_x)

    def get_y(self):
        return self.__y
          
    def set_y(self, y):
        self.__y = y

    y = property (get_y, set_y)

class Segment:
    def __init__(self, star_x, start_y, end_x, end_y):
        self.__start = Point(star_x, start_y)
        self.__end = Point(end_x, end_y)

    def get_start(self):
        return self.__start
    
    def set_start(self, star_x, start_y):
        self.__start = Point(star_x, start_y)

    start = property(get_start, set_start)

    def get_end(self):
        return self.__end

    def set_end(self, end_x, end_y):
        self.__end = Point(end_x, end_y)

    end = property(get_end, set_end)

 
    
