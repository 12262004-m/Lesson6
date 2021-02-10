class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self):
        a = self._width * self._length*25*5
        print("Масса асфальта равна ", a//1000, "т")
t=Road(int(input("Введите длину асфальта (в метрах): ")), int(input("Введите ширину асфальта(в метрах): ")))
t.massa()
