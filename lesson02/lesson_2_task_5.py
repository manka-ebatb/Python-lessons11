def month_to_season():
    n = int(input("Введите номер месяца "))
    if n in [1, 2, 12]:
        print("Сезон Зима!")
    elif n in [3, 4, 5]:
        print("Сезон Весна!")
    elif n in [6, 7, 8]:
        print("Сезон Лето!")
    elif n in [9, 10, 11]:
        print("Сезон Осень!")
    else:
        print("Такого месяца не существует")
