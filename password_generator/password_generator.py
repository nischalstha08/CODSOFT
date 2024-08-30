import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Length must be at least 1")

        characters = string.ascii_lowercase
        if upper_var.get():
            characters += string.ascii_uppercase
        if numbers_var.get():
            characters += string.digits
        if special_var.get():
            characters += string.punctuation
        
        if not characters:
            raise ValueError("At least one character set must be selected")

        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showwarning("Warning", "No password to copy")

# Initialize the main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")
root.configure(bg='#282C34')

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18), bg='#282C34', fg='#61AFEF')
title_label.pack(pady=10)

# Length Entry
length_frame = tk.Frame(root, bg='#282C34')
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Password Length:", font=("Helvetica", 14), bg='#282C34', fg='#ABB2BF')
length_label.pack(side=tk.LEFT, padx=5)

length_entry = tk.Entry(length_frame, font=("Helvetica", 14), width=10, bd=2, relief="solid")
length_entry.pack(side=tk.LEFT)

# Checkboxes for password complexity
complexity_frame = tk.Frame(root, bg='#282C34')
complexity_frame.pack(pady=10)

upper_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

upper_check = tk.Checkbutton(complexity_frame, text="Include Uppercase Letters", variable=upper_var, bg='#282C34', fg='#ABB2BF', font=("Helvetica", 12))
upper_check.grid(row=0, column=0, sticky="w", padx=5)

numbers_check = tk.Checkbutton(complexity_frame, text="Include Numbers", variable=numbers_var, bg='#282C34', fg='#ABB2BF', font=("Helvetica", 12))
numbers_check.grid(row=1, column=0, sticky="w", padx=5)

special_check = tk.Checkbutton(complexity_frame, text="Include Special Characters", variable=special_var, bg='#282C34', fg='#ABB2BF', font=("Helvetica", 12))
special_check.grid(row=2, column=0, sticky="w", padx=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 14), bg='#98C379', fg='#282C34', relief="raised", command=generate_password)
generate_button.pack(pady=10)

# Password Entry
password_frame = tk.Frame(root, bg='#282C34')
password_frame.pack(pady=10)

password_entry = tk.Entry(password_frame, font=("Helvetica", 14), width=30, bd=2, relief="solid")
password_entry.pack(side=tk.LEFT, padx=5)

# Copy Button
copy_button = tk.Button(password_frame, text="Copy", font=("Helvetica", 12), bg='#61AFEF', fg='#282C34', relief="raised", command=copy_to_clipboard)
copy_button.pack(side=tk.RIGHT, padx=5)

# Ensure button width is sufficient
copy_button.config(width=18)

# Run the application
root.mainloop()
