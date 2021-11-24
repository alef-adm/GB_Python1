incoming = int(input("Введите значение выручки:"))
outgoing = int(input("Введите значение издержек:"))
if incoming > outgoing:
    print(f"Поздравляю, Ваша прибыль составляет {incoming-outgoing} рублей")
elif incoming == outgoing:
    print("Вышли в 0, уже не плохо")
else:
    print(f"Очень жаль, но отчетный период завершился с убытком {outgoing-incoming} рублей")
print(f"Показатель рентабельности:{((incoming-outgoing)/incoming)}")
personal = int(input("Введите количество сотрудников:"))
print(f'Показатель прибыли в расчете на одного человека:{(incoming-outgoing)/personal} руб/чел')
