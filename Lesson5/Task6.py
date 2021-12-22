# Возможно использование re читерский ход, но я правда старался :)
# Я не разработчик, использую то что нахожу в Google, не судите строго :)


import re
import codecs


f = codecs.open("6.txt", "r", "utf_8_sig")
num1 = []
discipline = ""
sum1 = 0
dict1 = {}
temp_dict = {}

while True:
    line = f.readline()
    num1 = re.findall('\d+', line )
    discipline = (line.split(":")[0])
    for n in num1:
        sum1 += int(n)
    if len(discipline) > 0:
        temp_dict = {discipline: sum1}
        dict1.update(temp_dict)
        sum1 = 0
    else:
        print(dict1)

        break
