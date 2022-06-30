class Simpleton: pass

s2 = Simpleton()
s3 = Simpleton()

s = Simpleton()
print(s, type(s))
print(Simpleton, type(Simpleton))

s.test = 4
print(s.test)

s.print_test = lambda self: print(self.test)
s.print_test(s)

Simpleton.test = 77
print(Simpleton.test)
print(s.test)
print(s2.test)

Simpleton.test = 88
print(Simpleton.test)
print(s.test)
print(s2.test)

s2.test = 55
print(Simpleton.test)
print(s.test)
print(s2.test)

Simpleton.test = 99
print(Simpleton.test)
print(s.test)
print(s2.test)
print(s3.test)


class Student:

    name = ""
    year = 0
    speciality = ""

    def provide_self_info(self):
        print(f"I'm {self.name}, {self.speciality} student of the {self.year} year")

    def learn(self):
        print("I'm learning")

s1 = Student()
s1.name = "Mikita"
s1.year = 3
s1.speciality = "Agrotourism"

s2 = Student()
s2.name = "Luda"
s2.year = 4
s2.speciality = "Barista"

s1.provide_self_info()
s2.provide_self_info()
