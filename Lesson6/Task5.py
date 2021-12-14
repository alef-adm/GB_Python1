class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return 'Запуск отрисовки.'
class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки ручкой {self.title}'
class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки карандашом {self.title}'
class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки маркером {self.title}'

stat = Pencil('Parker')
print(stat.draw())
stat = Pen('Parker')
print(stat.draw())
stat = Handle('Parker')
print(stat.draw())
