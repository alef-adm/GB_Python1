class Matrix:
    def __init__(self, m1):
        self.m1 = m1


    def __str__(self):
        string1 = ''
        string2 = ''
        for list in self.m1:
            for num1 in list:
               string1 = string1+'%s\t' %(num1)
            string1 = string1[:-1]
            string1 = string1 + '\n'

        # for list2 in self.m2:
        #     for num2 in list2:
        #        string2 = string2+'%s\t' %(num2)
        #     string2 = string2[:-1]
        #     string2 = string2 + '\n'
        return str(string1)#,str(string2)
    def __add__(self, other):
        add = []
        for l1 in range(len(self.m1)):
            str = []
            for n1 in range(len(self.m1[l1])):
                str.append(self.m1[l1][n1] + other.m1[l1][n1])
            add.append(str)
        return Matrix(add)




a = [[1,2,3],[4,5,6],[7,8,9]]
m = Matrix(a)
print(m)
b = [[10,11,12],[13,14,15],[16,17,18]]
m2 = Matrix(b)
print(m2)
print(f'{m + m2}')