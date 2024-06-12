from time import sleep
from colorama import Fore, Style
from random import randint
def AutoType(text):
    list = [chr(i) for i in range(32,123)]
    value=""
    for i in text:
        for j in list:
            sleep(1/100)
            text_colors = [Fore.BLACK, Fore.RED ,Fore.GREEN ,Fore.YELLOW ,Fore.BLUE , Fore.MAGENTA ,Fore.CYAN,Fore.WHITE]
            color = randint(1,7)
            noise = chr(randint(32,123))
            n = noise if j!=text[-1] else "."
            print(text_colors[color] + Style.BRIGHT + f"{value + j + n}", end="\r" + Style.RESET_ALL)
            if j == i:
                value = value + j
                break
            value = value + " " if j == list[-1] else value


AutoType('My name is Shuaib')  # Change text for qoutation
sleep(5)