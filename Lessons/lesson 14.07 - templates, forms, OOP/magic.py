from argparse import ArgumentError


class FreightTrain:

    cart_len = 10

    def __init__(self, count):
        self.cart_len = count

    def __str__(self):
        return f"I'm a train of {self.cart_len} carts, choo-choo!!"

    def __int__(self):
        return self.cart_len

    def __add__(self, other):
        try:
            return FreightTrain(self.cart_len + other.cart_len)
        except:
            raise ArgumentError("Cannot add non-FreightTrain object")

    def __eq__(self, __o: object):
        if not isinstance(__o, FreightTrain):
            return False
        
        return self.cart_len == __o.cart_len

    def __len__(self):
        return self.cart_len*10

shorty = FreightTrain(3)
loooong = FreightTrain(12)

print(shorty)
print(loooong)

print(int(shorty))

print(shorty + loooong)
print(shorty == loooong)
print(shorty + loooong == FreightTrain(15))