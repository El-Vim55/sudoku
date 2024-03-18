import tkinter as tk
from tkinter import messagebox

def win_screen():
    messagebox.showinfo('', 'You Win!')
    root.destroy()

def duplicate_value():
    root = tk.Tk()
    root.withdraw()  # Hide the tkinter root window
    messagebox.showerror('', 'Duplicate Value')
    root.destroy()

def incorrect_values():
    messagebox.showwarning('', 'Incorrect Value')
    root.destroy()
