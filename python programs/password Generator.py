import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_letters, use_capital_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_lowercase
    if use_capital_letters:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if length < 8 or not characters:
        messagebox.showerror("Error", "Password length should be at least 8 characters and you must choose at least one character type.")
        return None
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def copy_password():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)

root = tk.Tk()
root.title("Password Generator")

password_label = tk.Label(root, text="Password")
password_label.grid(row=0, column=0)

password_entry = tk.Entry(root, width=40)
password_entry.grid(row=0, column=1)

length_label = tk.Label(root, text="Length")
length_label.grid(row=1, column=0)

length_spinbox = tk.Spinbox(root, from_=8, to=32)
length_spinbox.grid(row=1, column=1)

use_letters = tk.BooleanVar()
use_letters.set(True)
letters_checkbox = tk.Checkbutton(root, text="Lowercase Letters", variable=use_letters)
letters_checkbox.grid(row=2, column=0)

use_capital_letters = tk.BooleanVar()
use_capital_letters.set(True)
capital_letters_checkbox = tk.Checkbutton(root, text="Uppercase Letters", variable=use_capital_letters)
capital_letters_checkbox.grid(row=2, column=1)

use_numbers = tk.BooleanVar()
use_numbers.set(True)
numbers_checkbox = tk.Checkbutton(root, text="Numbers", variable=use_numbers)
numbers_checkbox.grid(row=2, column=2)

use_symbols = tk.BooleanVar()
use_symbols.set(True)
symbols_checkbox = tk.Checkbutton(root, text="Symbols", variable=use_symbols)
symbols_checkbox.grid(row=2, column=3)

generate_button = tk.Button(root, text="Generate", command=lambda: password_entry.delete(0, tk.END) or password_entry.insert(0, generate_password(int(length_spinbox.get()), use_letters.get(), use_capital_letters.get(), use_numbers.get(), use_symbols.get())))
generate_button.grid(row=3, column=0)

copy_button = tk.Button(root, text="Copy", command=copy_password)
copy_button.grid(row=3, column=1)

root.mainloop()