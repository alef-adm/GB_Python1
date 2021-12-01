list1 = input("Введите несколько чисел через пробел:")
split1 = list1.split()
s = float(0)
for n in split1:
    n = float(n)
    s += n
try:
    list2 = input("Есле хотите продолжить введите цифры, если не хотите любой другой символ:")
    split2 = list2.split()
    for n2 in split2:
        n2 = float(n2)
        s += n2
except ValueError:
    print(s)
#