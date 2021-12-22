import codecs
import csv
with open("t3.txt") as f:
    reader = csv.reader(f, delimiter=" ")
    data = list(reader)
i = 0
low_sal = []
average = 0
for people in data:
    average += int(people[1])
    i += 1
    if int(people[1]) < 20000:
        low_sal.append(people[0])
print(f'Зп ниже 20000 у {low_sal}')
print(f'средняя зарплата {average/i}')
