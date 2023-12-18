import tkinter as tk
import time
import threading
from pynput.mouse import Controller, Button, Listener

delay = 0.001
button = Button.left
toggle_button = Button.x1  # 마우스 4번 버튼
macro_active = False

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        if not self.running:
            self.running = True

    def stop_clicking(self):
        if self.running:
            self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

def on_click(x, y, btn, pressed):
    global macro_active
    if btn == toggle_button and not pressed:
        if not macro_active:
            click_thread.start_clicking()
            macro_active = True
        else:
            click_thread.stop_clicking()
            macro_active = False

def on_release(key):
    if key == toggle_button:
        click_thread.stop_clicking()

def on_close():
    click_thread.exit()
    root.destroy()

# 인스턴스 생성
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

# GUI 생성
root = tk.Tk()
root.title("Click Macro")

# 키 및 마우스 이벤트 리스너 시작
with Listener(on_click=on_click, on_release=on_release) as listener:
    root.mainloop()
    listener.join()
