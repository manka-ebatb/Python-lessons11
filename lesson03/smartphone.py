class Smartphone:

    def __init__(self, a, b, n):
        print("Смартфон сохранен в каталог")
        self.a = a
        self.b = b
        self.n = n

    def info(self):
        print("Информация о смартфоне ", self.a, "-", self.b, ".", self.n)
