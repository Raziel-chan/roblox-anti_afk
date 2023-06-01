import threading
import time
import pyautogui
from pynput import keyboard
import logging
anti_afk = False


logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# Then, in your functions:

class KeyListener:
    def __init__(self):
        self.shift_pressed = False
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )

    def on_press(self, key):
        if key == keyboard.Key.shift:
            self.shift_pressed = True
        elif self.shift_pressed and key == keyboard.KeyCode.from_char('P'):
            global anti_afk
            if anti_afk:
                print("anti-afk is off")
                anti_afk = False
            else:
                print("anti-afk is on")
                anti_afk = True
        elif self.shift_pressed and key == keyboard.KeyCode.from_char('Q'):
            self.listener.stop()
        else:
            self.shift_pressed = False

    def on_release(self, key):
        if key == keyboard.Key.shift:
            self.shift_pressed = False

    def start(self):
        self.listener.start()


def thread_function_anti_afk():
    global anti_afk

    while True:
        if anti_afk:
            pyautogui.press('w')
            pyautogui.press('space')
            pyautogui.click()
            time.sleep(2)

try:
    if __name__ == "__main__":
        print("Welcome to roblox anti-afk!")
        print("Commandes :")
        print("1- Shift + p to pause/unpause")
        print("2- shift + q to quit")
        kl = KeyListener()
        thread_anti_afk = threading.Thread(target=thread_function_anti_afk)
        thread_anti_afk.daemon = True
        thread_anti_afk.start()
        kl.start()
        kl.listener.join()
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
