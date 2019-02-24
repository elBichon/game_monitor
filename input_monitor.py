from pynput import mouse
from pynput import keyboard
from utils import *

lis1 = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)

lis2 = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)

lis1.start()
lis2.start()
lis1.join()
lis2.join()



