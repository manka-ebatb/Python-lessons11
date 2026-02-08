from smartphone import Smartphone

phone_1 = Smartphone("Vivo", "cX5", "+79364587694")
phone_2 = Smartphone("iPhone", "5SE", "+79658456321")
phone_3 = Smartphone("Xiaomi", "Redmi 10", "+79482145874")
phone_4 = Smartphone("Infinix", "Cristall Glass", "+79325481452")
phone_5 = Smartphone("TEHNO", "rt89D", "+79651287891")

catalog = [phone_1, phone_2, phone_3, phone_4, phone_5]

for x in range(0, 5):
    catalog[x].info()
