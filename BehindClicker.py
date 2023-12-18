import time
import win32gui
import win32con
import threading
from pynput.mouse import Listener, Controller, Button
import tkinter as tk
from tkinter import ttk
import winsound

delay = 0.001
button = Button.left
start_stop_button = Button.x1  # 마우스 4번 버튼

class CloTiZen:
    def __init__(self):
        self.win_title_name = "ArkAscended"
        self.handle = win32gui.FindWindow(None, self.win_title_name)
        self.mouse = Controller()
        self.click_thread = None
        self.running = False

        # GUI 설정
        self.root = tk.Tk()
        self.root.title("CloTiZen Auto-Clicker")
        self.root.geometry("300x100")

        self.start_button = ttk.Button(self.root, text="Start (mouse4)", command=self.start_clicking)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = ttk.Button(self.root, text="Stop (beep sound)", command=self.stop_clicking, state="disabled")
        self.stop_button.pack(side="right", padx=10)

    def start_clicking(self):
        self.running = True
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"

        while self.running:
            win32gui.SendMessage(self.handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
            time.sleep(delay)
            win32gui.SendMessage(self.handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
            time.sleep(delay)

        winsound.Beep(1000, 200)  # 클릭 중지 시 beep 소리

    def stop_clicking(self):
        self.running = False
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"

        winsound.Beep(200, 300)  # 클릭 중지 시 beep 소리

    def on_click(self, x, y, btn, pressed):
        if btn == start_stop_button and pressed:
            if self.click_thread and self.click_thread.is_alive():
                self.stop_clicking()
                self.click_thread.join()
                self.click_thread = None
            else:
                self.click_thread = threading.Thread(target=self.start_clicking)
                self.click_thread.start()

    def start_listener(self):
        with Listener(on_click=self.on_click) as listener:
            listener.join()

    def run_gui(self):
        self.root.mainloop()

if __name__ == "__main__":
    clo_ti_zen = CloTiZen()
    threading.Thread(target=clo_ti_zen.start_listener).start()
    clo_ti_zen.run_gui()
