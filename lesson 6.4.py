from colorama import Fore, Back, Style

class Car:
    def init(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def go(self):
        return f'{Back.WHITE}{Fore.BLACK} Машина поехала!'

    def stop(self):
        return f"{Back.WHITE}{Fore.BLACK} Машина остановилась!"

    def turn(self, direction):
        return f"{Back.WHITE}{Fore.BLACK} Вы повернули {direction}"

    def show_speed(self):
        return self.speed
class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            return f"{Back.CYAN}{Fore.RED} Превышение скорости! Сбросте скорость!"
        else:
            return f"{Fore.GREEN} Ваша скорость в норме!"

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            return f"{Back.CYAN}{Fore.RED} Превышение скорости! Сбросте скорость!"
        else:
            return f"{Fore.GREEN} Ваша скорость в норме!"

class PoliceCar(Car):
    pass

a = TownCar("Mersedes Benz", "черная", "90")
print(a.go(), a.show_speed(), a.turn("налевo"), a.stop())
b = SportCar("Aidi Q5", "оранжевая", "70")
print(b.go(), b.show_speed(), b.turn("налево"), b.stop())
c = WorkCar("Subaru Forester", "голубая", "60")
print(c.go(), c.show_speed(), c.turn("направо"), c.stop())
d = PoliceCar("Hundai Solaris", "белая", "55")
print(d.go(), d.show_speed(), d.turn("направо"), d.stop())




