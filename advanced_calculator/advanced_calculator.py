import tkinter as tk
from tkinter import messagebox
import math

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to clear the last character
def clear_last():
    current_text = entry.get()
    new_text = current_text[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_text)

# Function to add function button value to entry
def button_click(value):
    entry.insert(tk.END, value)

# Function to perform square root calculation
def sqrt():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to perform percentage calculation
def percentage():
    try:
        value = float(entry.get())
        result = value / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Initialize the main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x500")
root.configure(bg='#2E2E2E')

# Create an Entry widget for user input
entry = tk.Entry(root, font=("Arial", 20), bd=5, insertwidth=2, width=16, justify='right', bg='#F5F5F5', fg='#333')
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

# Define button layout and create buttons
buttons = [
    ('7', '8', '9', '/', '√'),
    ('4', '5', '6', '*', '%'),
    ('1', '2', '3', '-', 'C'),
    ('0', '.', '=', '+', 'CE')
]

# Function to create buttons
def create_button(text, row, col, command, width=5, height=2):
    return tk.Button(root, text=text, padx=width, pady=height, font=("Arial", 14), bg='#333', fg='#FFF', command=command)

# Add buttons to the grid
for row_index, row in enumerate(buttons):
    for col_index, button in enumerate(row):
        if button == '=':
            btn = create_button(button, row_index + 1, col_index, calculate, width=10)
        elif button == 'C':
            btn = create_button(button, row_index + 1, col_index, clear, width=10)
        elif button == 'CE':
            btn = create_button(button, row_index + 1, col_index, clear_last, width=10)
        elif button == '√':
            btn = create_button(button, row_index + 1, col_index, sqrt, width=5)
        elif button == '%':
            btn = create_button(button, row_index + 1, col_index, percentage, width=5)
        else:
            btn = create_button(button, row_index + 1, col_index, lambda b=button: button_click(b))
        btn.grid(row=row_index + 1, column=col_index, sticky="nsew")

# Adjust column and row weights for resizing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i + 1, weight=1)

# Run the application
root.mainloop()
