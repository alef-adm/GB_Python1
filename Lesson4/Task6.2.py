from sys import argv
from itertools import cycle


l1 = [1, 2, 3]
script_name, repeats = argv
repeats = int(repeats)
i = 1
for el in cycle(l1):
    if i > repeats:
        break
    print(el)
    i += 1

