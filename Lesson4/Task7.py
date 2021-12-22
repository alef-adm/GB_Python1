def fact(n):
    f = 1
    for i in range(1, n):
        f = f*i
        yield f


fa = fact(8)
for el in fa:
    print(el)
