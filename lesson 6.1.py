from time import sleep
import colorama
from colorama import Fore, Back, Style
colorama.init()
class Traffic:
    color = ["red", "yellow", "green"]
    def traf(self):
        i = 0
        while i!=3:
            if i == 0:
                print(Fore.RED + Traffic.color[0])
                sleep(7)
            if i == 1:
                print(Fore.YELLOW + Traffic.color[1])
                sleep(2)
            if i == 2:
                print(Fore.GREEN + Traffic.color[2])
                sleep(7)
            i+=1
t=Traffic()
t.traf()

