new = ""
out_list = []
with open("t4.txt") as file:
    for line in file:
        line = line.split('-')
        if line[0] == "One":
            new = "Один-1\n"
            out_list.append(new)
        elif line[0] == "Two":
            new = "Два-1\n"
            out_list.append(new)
        elif line[0] == "Three":
            new = "Три-1\n"
            out_list.append(new)
        elif line[0] == "Four":
            new = "Четыре-1\n"
            out_list.append(new)
        elif line[0] == "Five":
            new = "Пять-1\n"
            out_list.append(new)
with open("t4-1.txt", "w", encoding="utf8") as file2:
    file2.writelines(out_list)
