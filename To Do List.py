from tkinter import *
import tkinter.messagebox
import time

root = tkinter.Tk()
root.title("To-Do List")

print("How much time do you want to put? (min)")
#improve
def timer():
    try:
        countdown = float(entry_time.get())
        countdown = countdown * 60
        time.sleep(countdown)
        tkinter.messagebox.showwarning(title = "Congrats", message = "Time is up")
    except ValueError:
        tkinter.messagebox.showwarning(title = "Error", message = "Please enter a time")
        checkbox1.deselect()
        checkbox2.deselect()
        checkbox3.deselect()

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

entry_time = tkinter.Entry(root)
entry_time.config(font=("Courier", 30))
entry_time.pack()

checkbox1 = Checkbutton(root, text = "Research Networking for IB", width = 50, command = timer, anchor = 'w')
checkbox1.config(font=("Courier", 30))
checkbox1.pack()

checkbox2 = Checkbutton(root, text = "youROK", width = 50, command = timer, anchor = 'w')
checkbox2.config(font=("Courier", 30))
checkbox2.pack()

checkbox3 = Checkbutton(root, text = "Meditation", width = 50, command = timer, anchor = 'w')
checkbox3.config(font=("Courier", 30))
checkbox3.pack()

#creates the window
root.mainloop()
