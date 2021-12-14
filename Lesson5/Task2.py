import codecs
f = codecs.open("t2.txt", "r", "utf_8_sig")
s_count = 0
w_count = 0
string = "1"
while True:
    #s = f.read(1024)
    line = f.readline()
    for word in line.split():
        w_count += 1
    if w_count > 0:
        print(f'{line} Количество слов {w_count}')
    if w_count == 0:
        f.close()
        break
    w_count = 0




