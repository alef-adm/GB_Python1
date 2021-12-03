my_str = input("Введите несколько слов через пробел:")
split_result = my_str.split(sep=' ')
i = 1
for word in split_result:
    print(f'{i}. {word[0:10]}')
    i+=1
#один два три четыре длывадлоыдваоыдлоадылоалыовадлоыва
#
