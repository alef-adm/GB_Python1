class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data1 = input("Введите число: ")
inp_data2 = input("Введите число не равное нулю: ")

try:
    inp_data1 = int(inp_data1)
    inp_data2 = int(inp_data2)

    if inp_data2 == 0:
        raise OwnError("Вы ввели 0!")
    res = inp_data1 / inp_data2

except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {res}")

