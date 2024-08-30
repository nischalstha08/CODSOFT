import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        # GUI Elements
        self.task_input = tk.Entry(root, width=50)
        self.task_input.grid(row=0, column=0, padx=10, pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10)

        self.task_listbox = tk.Listbox(root, width=60, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.grid(row=2, column=0, padx=10, pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=1, padx=10, pady=5)

    def add_task(self):
        task = self.task_input.get()
        if task != "":
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task!")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[Completed]" if task["completed"] else "[Pending]"
            self.task_listbox.insert(tk.END, f"{task['task']} {status}")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task!")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task!")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
