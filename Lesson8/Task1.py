class Data:
    @classmethod
    def one(cls,data):
        d_list = data.split('-')
        day = int(d_list[0])
        month = int(d_list[1])
        year = int(d_list[2])
        print(f'День - {day}, месяц - {month}, год - {year}')
    @staticmethod
    def two(data1):
        d_list = data1.split('-')
        day = int(d_list[0])
        month = int(d_list[1])
        year = int(d_list[2])
        if day < 0 or day > 31:
            print("таких дат не существует, максимальное количество дней 31")
        elif month<0 or month>12:
            print("Такого месяца не существует")
        elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if month == 2 and day > 28:
                print("неверная дата, в феврале високосного года 28 дней.")
        elif month == 2 and day > 27:
            print("Неверная дата, обычно в феврале 27 дней")
        elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
            print("неверная дата, в этом месяце максимум 30 дней ")
        else:
            print("дата корректна")



Data.one("12-12-2012")
print(Data.two("30-12-2021"))
