import json
import re

i = 0
sum1 = 0
stat = {}
with open("t7.txt", "r", encoding="utf8") as f:
    for line in f:
        num_list = re.findall('\d+', line)
        firm = (line.split())[0]
        in1 = int(num_list[1])
        out1 = int(num_list[2])
        stat.update({firm:(in1-out1)})

        if in1 > out1:
            sum1 = sum1+(in1 - out1)
            i += 1
    avg = int(sum1/i)
    list1 = [stat,{'average_profit':avg}]
    print(list1)
with open("t7.json", "w") as write_file:
    json.dump(list1, write_file)
