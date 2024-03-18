import tkinter as tk
from tkinter import messagebox

def win_screen():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo('', 'You Win!')
    root.destroy()

def incomplete_grid():
    root = tk.Tk()
    root.withdraw() 
    messagebox.showerror('', 'Grid Incomplete!')
    root.destroy()   

def duplicate_value():
    root = tk.Tk()
    root.withdraw() 
    messagebox.showerror('', 'Duplicate Value!')
    root.destroy()

def incorrect_values():
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning('', 'Incorrect Value!')
    root.destroy()
