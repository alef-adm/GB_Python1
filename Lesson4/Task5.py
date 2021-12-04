from functools import reduce


# l1 = [el for el in range(100, 1001, 2)]
def func1(prev, el):
    return prev*el


print(reduce(func1, [el for el in range(100, 1001, 2)]))
