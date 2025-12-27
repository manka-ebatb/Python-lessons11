def leap(a):
    return True if a % 4 == 0 else False
def is_year_leap():
    a = int(input("Введите год "))
    print("Год", a, ":", leap(a))
is_year_leap()
