class OwnError(Exception):
    def __init__(self):
        self.txt = "Просили же ЧИСЛО!"
num_list = []
while True:
    var = input("Введите число, если хотите остановиться введите S:")
    try:
        if var.isdigit():
           num_list.append(var)

        elif var == "S":
            print(num_list)
            break

        else:
            raise OwnError

    except OwnError as err:
        print(err.txt)