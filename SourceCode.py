import keyboard
from colorama import *
import time

init()

def guide(a, b):
    print(Fore.CYAN + '=========================')
    print(Fore.YELLOW + f'{a}하려면 {b} 키 누르기')
    print(Fore.CYAN + '=========================')
    return

idk=input(Fore.GREEN  + '도배할 말을 입력해주세요 : ')
guide('시작', 'f6')
while 6974:
    try:
        if keyboard.is_pressed('f6'):
            guide('종료', 'f7')
            while 6974:
                if keyboard.is_pressed('f7'):
                    print(Fore.RED + '종료됨')
                    guide('다시 시작', 'f6')
                    break
                keyboard.write(idk)
                keyboard.press('Enter')
                time.sleep(0.2)
    except  Exception as e:
        print(e)
        input('엔터  누르면 종료')
        break


