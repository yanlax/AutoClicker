import keyboard
import mouse
import time
from win10toast import ToastNotifier

Timeng = float(input(' Введите тайминги: '))
Click = input(' Какую кнопку: (left,right) ')
print(" Для активации нажмите сочитание клавишь: (Alt + Z) ")

isClicking = False 

def show_notify(title, text):
    toast = ToastNotifier()
    toast.show_toast(title, text, duration = 5, icon_path = "icon.ico")

def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        show_notify("Clicker","Clicker off ")
    else:
        isClicking = True
        show_notify("Clicker","Clicker on ")

keyboard.add_hotkey('Alt + Z', set_clicker)

while True:
    if isClicking:
        mouse.click(button = 'left')
        time.sleep(Timeng)
