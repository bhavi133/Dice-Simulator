import random
import tkinter as tk

window = tk.Tk()
window.title("Dice Simulator")
window.geometry("600x300")

l1 = tk.Label(window, text="", font=("arial", 300))

def roll_the_dice():
    num_code = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f"{random.choice(num_code)}{random.choice(num_code)}")
    l1.pack()

b1 = tk.Button(window, text="Roll the dice!", command=roll_the_dice)
b1.place(x=250, y=0)

window.mainloop()
