l1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
l2 = []
temp1 = None
stub = 0
for i in l1:
    if temp1 == None:
        temp1 = i
        print(temp1)
    elif i < temp1:
        temp1 = i
    elif i > temp1:
        l2.append(i)
        temp1 = i
print(l2)

    #     print(temp1)
    # elif i > temp1:
    #     l2.append(i)
    #     print(l2)
    # else:
    #     stub+=1


