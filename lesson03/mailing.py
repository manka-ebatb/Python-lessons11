from address import Address


class Mailing:
    def __init__(self, u: Address, x: Address, y: int, z: str):
        print("Отправление зарегестрировано")
        self.u = u
        self.x = x
        self.y = y
        self.z = z

    def info(self):
        print("Отправление ", self.z, "из ", end=' ')
        self.u.printAddress()
        print("в ", end=' ')
        self.x.printAddress()
        print(".", end=' ')
        print("Стоимость ", self.y, " рублей.")

    def getMailing(self):
        return Mailing
