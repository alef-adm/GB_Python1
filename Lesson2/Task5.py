my_list = []
while True:
    data = input("Введите значение:")
    if len(data) > 0:
        my_list.append(data)
    else:
        break
my_list.sort(reverse=True)
print(my_list)
