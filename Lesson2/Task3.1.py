month = int(input("Введите номер месяца:"))
if month < 1 or month > 12:
    print("Кого вы пытаетесь обмануть...")
    exit()
y = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
sel = month - 1
if y[sel] in "ДекабрьЯнварьФевраль":
    print("Время года - зима")
elif y[sel] in "МартАпрельМай":
    print("Время года - весна")
elif y[sel] in "ИюньИюльАвгуст":
    print("Время года - лето")
else:
    print("Время года - осень")
