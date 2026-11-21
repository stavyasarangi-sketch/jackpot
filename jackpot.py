import random
import tkinter as tk
from tkinter import font
import tkinter.messagebox

def spin_slots():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)

    slot1_label.config(text=str(num1))
    slot2_label.config(text=str(num2))
    slot3_label.config(text=str(num3))

    game_window.update()

    if num1 == num2 and num2 == num3:
        tkinter.messagebox.showinfo("Jackpot!", "JACKPOT! You win $1000!")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        tkinter.messagebox.showinfo("Mini Prize", "Mini Prize! You win $10!")
    else:
        tkinter.messagebox.showwarning("Loss", "Bad Luck! Try Again.")

game_window = tk.Tk()
game_window.title("Lucky Slots")
game_window.geometry("400x250")

slot_font = font.Font(size=30)
btn_font = font.Font(size=14)

slots_frame = tk.Frame(game_window)
slots_frame.pack(pady=30)

slot1_label = tk.Label(slots_frame, text="0", font=slot_font)
slot1_label.grid(row=0, column=0, padx=20)

slot2_label = tk.Label(slots_frame, text="0", font=slot_font)
slot2_label.grid(row=0, column=1, padx=20)

slot3_label = tk.Label(slots_frame, text="0", font=slot_font)
slot3_label.grid(row=0, column=2, padx=20)

spin_btn = tk.Button(
    game_window, text="SPIN", width=12, font=btn_font, command=spin_slots
)
spin_btn.pack(pady=10)

game_window.mainloop()
