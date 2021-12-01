def sum(a, b, c):
    if a < b and a < c:
        s = b + c
    elif b < a and b < c:
        s = a + c
    elif c < a and c < b:
        s = a + b
    return s


print(sum(7, 8, 3))

#