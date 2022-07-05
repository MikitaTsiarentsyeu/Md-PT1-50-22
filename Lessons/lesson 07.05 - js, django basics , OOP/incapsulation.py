class Student:

    __year = 1

    def __init__(self, name, year, speciality):
        self.__name = name
        self.year = year
        self.__speciality = speciality

    def get_name(self):
        return self.__name

    def get_speciality(self):
        return self.__speciality.upper()

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if year < 6:
            self.__year = year

    year = property(get_year, set_year)
    name = property(get_name)

    def provide_self_info(self):
        print(f"I'm {self.name}, {self.get_speciality()} student of the {self.year} year")

    def learn(self):
        print("I'm learning")

s = Student("Mikita", 555, "cakes cooking")
s.provide_self_info()
# s.year = 100
# print(s.year)

# s.set_student("Mikita", 5, "cakes cooking")

s.set_year(100)
print(s.get_year())

# print(s.year) error
# print(s._Student__year)

s.year = 4
print(s.year, s.name)
s.name = "test"