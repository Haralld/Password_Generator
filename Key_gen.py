# Description:
# This Python program provides a graphical user interface (GUI) for generating secure passwords.
# Users can specify the password length and choose whether to include lowercase letters, uppercase letters, digits, and specific symbols (!, ?, _).
# The application dynamically adapts to window resizing, ensuring that text and layout scale appropriately.
# Built with the Tkinter library, it demonstrates practical GUI design and dynamic content scaling in Python.


import tkinter as tk
from tkinter import ttk
import random

def generate_password():
    length = int(length_entry.get())
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    characters = ''
    if use_lowercase:
        characters += 'abcdefghijklmnopqrstuvwxyz'
    if use_uppercase:
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_digits:
        characters += '0123456789'
    if use_symbols:
        characters += '!?_'

    if not characters:
        result_var.set("Select at least one option!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

def resize_text(event):
    new_size = max(10, int(min(event.width, event.height) / 25))
    style.configure("TLabel", font=("TkDefaultFont", new_size))
    style.configure("TButton", font=("TkDefaultFont", new_size))
    style.configure("TCheckbutton", font=("TkDefaultFont", new_size))

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)  # Allow the window to be resizable

# Define variables
length_var = tk.IntVar(value=8)
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

# Configure styles
style = ttk.Style()
style.configure("TLabel", font=("TkDefaultFont", 12))
style.configure("TButton", font=("TkDefaultFont", 12))
style.configure("TCheckbutton", font=("TkDefaultFont", 12))

# Create widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky=tk.W)

length_entry = ttk.Entry(frame, textvariable=length_var, width=20)
length_entry.grid(row=0, column=1, sticky=tk.W)

options_frame = ttk.Frame(frame)
options_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

lowercase_check = ttk.Checkbutton(options_frame, text="Lowercase Letters", variable=lowercase_var)
lowercase_check.grid(row=0, column=0, sticky=tk.W)

uppercase_check = ttk.Checkbutton(options_frame, text="Uppercase Letters", variable=uppercase_var)
uppercase_check.grid(row=1, column=0, sticky=tk.W)

digits_check = ttk.Checkbutton(options_frame, text="Digits", variable=digits_var)
digits_check.grid(row=0, column=1, sticky=tk.W)

symbols_check = ttk.Checkbutton(options_frame, text="Symbols (!, ?, _) ", variable=symbols_var)
symbols_check.grid(row=1, column=1, sticky=tk.W)

result_label = ttk.Label(frame, text="Generated Password:")
result_label.grid(row=3, column=0, sticky=tk.W)

result_entry = ttk.Entry(frame, textvariable=result_var, width=30)
result_entry.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))

generate_button = ttk.Button(frame, text="Generate", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2)

# Configure resizing behavior
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Bind resize event to update text size
root.bind("<Configure>", resize_text)

# Configure padding
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()