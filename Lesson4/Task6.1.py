from sys import argv
from itertools import count


scipt_name, start, end = argv
start = int(start)
end = int(end)
for el in count(start):
    if el < end:
        print(el)
    else:
        break
