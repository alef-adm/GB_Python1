class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return (int(self.income["wage"])+int(self.income["bonus"]))


my_people = Position("Ivan", "Ivanov", "engineer", 2000, 500)
print(my_people.get_full_name())
print(my_people.get_total_income())
