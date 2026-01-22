class Address:

    def __init__(self, a, b, c, d, e):
        print("Адрес: ", a, b, c, d, e, "добавлен")
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def printAddress(self):
        print(self.a, self.b, self.c, self.d, self.e, end=' ')

    def getAddress(self):
        return Address
