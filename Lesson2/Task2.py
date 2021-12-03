my_list = []
while True:
    data = input("Введите значение:")
    if len(data) > 0:
        my_list.append(data)
    else:
        break
repeats = len(my_list) // 2
key = 0
i = 1
while i <= repeats:
    a = key
    key += 1
    b = key
    my_list[a], my_list[b] = my_list[b], my_list[a]
    key += 1
    i += 1
print(my_list)
#