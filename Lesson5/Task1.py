file_name = input("Введите имя файла и расширение:")
my_file = open(file_name, "w+")
my_file.close()
my_string = input("Введите любую строку и нажмите Enter:")
my_string += "\n"
my_data = [my_string]
while len(my_string) > 0:
    my_string = input("Введите еще одну строку, если не хотите нажмите Enter:")
    if len(my_string) > 0:
        my_string += "\n"
        my_data.append(my_string)
for s in my_data:
    my_file = open(file_name, "a+")
    my_file.write(s)
    my_file.close()
