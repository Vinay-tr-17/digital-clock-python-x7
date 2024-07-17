from tkinter import *
import time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, update_time)
root = Tk()
root.title("Digital Clock")
root.geometry("400x200")
clock = Label(root, font=("Helvetica", 48, "bold"), bg="white")
clock.pack(pady=20)
update_time()
root.mainloop() 