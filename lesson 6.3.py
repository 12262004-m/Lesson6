class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(input("Введите оклад: ")), "bonus": int(input("Введите премию:")) }
class Position(Worker):
    def get_full_name(self):
        print("Полное имя сотрудника: ", self.name, self.surname)
    def get_total_income(self):
        print("Доход сотрудника: ", self._income["wage"] + self._income["bonus"])

t=Position(input("Введите имя сотрудника: "), input("Введите фамилию сотрудника: "), input("Введите должность сотрудника: "))
t.get_full_name()
t.get_total_income()