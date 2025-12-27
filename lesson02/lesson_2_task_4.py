def fizz_buzz(n):
    for z in range(1, n+1):
        if z % 5 == 0 and z % 3 == 0:
            print("fizzbuzz")
        elif z % 3 == 0:
            print("fizz")
        elif z % 5 == 0:
            print("buzz")
        else:
            print(z)