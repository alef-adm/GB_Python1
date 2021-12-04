l1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
l2 = []
res = 0
for i in l1:
    for j in l1:
        #print(i,j)
        if i == j:
            res +=1
    if res == 1:
        l2.append(i)
    res = 0
print(l2)

