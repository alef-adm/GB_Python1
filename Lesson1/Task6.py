f = int(input("Укажите первое значение в км:"))  # f - first
r = int(input("Укажите целевое значение в км:"))  # r - required
i = 0  # counter
d = f  # промежуточное значение
while d < r:
    d = d + d/10
    i = i + 1
print(f"На {i}-й день спортсмен достиг результата - не менее {r} км")
#finish
