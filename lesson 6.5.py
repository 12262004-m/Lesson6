class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки " + self.title)
class Pensil(Stationery):
    def draw(self):
        print("Запуск отрисовки " + self.title)


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки " + self.title)


a = Pen("карандашом")
b = Pensil("ручкой")
c = Handle("маркером")

a.draw()
b.draw()
c.draw()