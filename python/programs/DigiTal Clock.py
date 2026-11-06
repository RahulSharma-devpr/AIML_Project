from tkinter import *
import time

root = Tk()
root.title("Digital Clock BY RS")
root.geometry("300x200")

# Optional: display current time
def show_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, show_time)  # update every 1 sec

label = Label(root, font=('calibri', 55,'bold'), background='red',foreground='black')
label.pack(pady=50)

show_time()
root.mainloop()
