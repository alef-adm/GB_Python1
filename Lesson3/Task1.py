def division(a, b):
    if b == 0:
        b = int(input("Попробуй еще раз ввести число не равное 0:"))
    d = a / b
    return d


print(division(int(input("Введи любое число:")), int(input("Введи число не равное 0:"))))
