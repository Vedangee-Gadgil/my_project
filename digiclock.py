import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    root.after(1000, update_time) 

root = tk.Tk()
root.title("Digital Clock")


label = tk.Label(root, font=('ds-digital', 100))
label.pack()


update_time()


root.mainloop()
