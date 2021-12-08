file_name = input("Введите имя файла и расширение:")
my_file = open(file_name, "w+")
my_file.close()
my_string = input("Введите несколько цифр через пробел и нажмите Enter:")
my_file = open(file_name, "a+")
my_file.write(my_string)
my_file.close()
# my_data = [my_string]
total = 0
my_data = my_string.split()
for num in my_data:
    total += int(num)
print(total)

