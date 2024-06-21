import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(entry.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive integer.")
            return
        password = generate_password(length)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Enter the desired length for the password:").pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
