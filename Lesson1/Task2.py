seconds = input("Введи количество секунд, да побольше!:")
h = int(seconds)//3600
m = (int(seconds) % 3600)//60
s = (int(seconds) % 3600) % 60
print(f"{h}:{m}:{s}")
