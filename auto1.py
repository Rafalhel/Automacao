import time
from datetime import date
import pyautogui

seg1 = 97008923329
seg2 = 91281210707
ter1 = 98697198016
ter2 = 94416817691
qua1 = 92904660131
sex1 = 92109319047
sex2 = 98111556931
hj = date.today()
hj.weekday()
h = int(time.strftime('%H', time.localtime()))
m = int(time.strftime('%M', time.localtime()))
v = 0
if hj.weekday() == 0:
    if h == 18 or h == 19 or h == 20 and m < 25:
        v = seg1
        print("Aula de 'ALPOO LAB' com o professor Alécio")
        print("Tenha uma boa aula!")
    elif h == 20 and m > 25 or h == 21:
        v = seg2
        print("Aula de 'ALPOO LAB' com o professor Alécio")
        print("Tenha uma boa aula!")
elif hj.weekday() == 1:
    if h == 18 or h == 19 or h == 20 and m < 25:
        v = ter1
        print("Aula de 'LPBD' com o professor Robson")
        print("Tenha uma boa aula!")
    elif h == 20 and m > 25 or h == 21:
        v = ter2
        print("Aula de 'LPBD LAB' com o professor Robson")
        print("Tenha uma boa aula!")
elif hj.weekday() == 2:
    if h == 18 or h == 19 or h == 20 and m < 25:
        v = qua1
        print("Aula de 'ALPOO LAB' com o professor Gustavo")
        print("Tenha uma boa aula!")
elif hj.weekday() == 4:
    if h == 18 or h == 19 or h == 20 and m < 25:
        v = sex1
        print("Aula de 'ED' com o professor Gley")
        print("Tenha uma boa aula!")
    elif h == 20 and m > 25 or h == 21:
        v = sex2
        print("Aula de 'ED LAB' com o professor Gley e Pedro")
        print("Tenha uma boa aula!")
elif hj.weekday() == 5:
    print("Hoje é Sábado")
    print("Não tem aula!")
    input("Aperte ENTER para finalizar!")
elif hj.weekday() == 6:
    print("Hoje é Domingo")
    print("Não tem aula!")
    input("Aperte ENTER para finalizar!")
else:
    v = 0


if v == 0:
    time.sleep(2)


else:
    time.sleep(2)
    pyautogui.click(770, 750)
    time.sleep(1)
    pyautogui.click(700, 360)
    time.sleep(1.5)
    pyautogui.typewrite(str(v))
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("delete")
    pyautogui.typewrite("Rafael Gomes D919HH-7 CC4P-68")
    pyautogui.hotkey("enter")
    time.sleep(5)

