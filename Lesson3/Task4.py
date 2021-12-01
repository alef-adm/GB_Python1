def exponentiation(x, y):
    if x < 0:
        while x < 0:
            x = float(input("Попробуй еще раз ввести ПОЛОЖИТЕЛЬНОЕ число:"))
    if y > 0:
        while y >0:
            y = int(input("Нужно ЦЕЛОЕ ОТРИЦАТЕЛЬНОЕ число:"))
    exp = x**y
    return exp


print(exponentiation(float(input("Введи любое положительное число:")), int(input("Введи целое отрицательное число:"))))
