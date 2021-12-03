my_list = [7, 5, 3, 3, 2]
data = int(input("Введите значение:"))
length = len(my_list)
i = 0
length = length - 1
#print(length)
while i <= length:
    #print(my_list[i])
    if data > my_list[i]:
        #print(length)
        my_list.insert(i, data)
        break
    elif i == length:
        my_list.insert(i+1, data)
    i += 1
print(my_list)