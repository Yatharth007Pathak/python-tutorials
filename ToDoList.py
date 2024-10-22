import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def clear_all_tasks():
    listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("To-Do List Application")

# Create widgets
entry = tk.Entry(root, width=50)
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks)
listbox = tk.Listbox(root, width=50, height=10)

# Layout widgets
entry.pack(pady=10)
add_button.pack(pady=5)
delete_button.pack(pady=5)
clear_button.pack(pady=5)
listbox.pack(pady=10)

# Run the application
root.mainloop()

'''
Here's a pointwise breakdown of the code, line by line:

import tkinter as tk:
Import the Tkinter module and refer to it as tk. Tkinter is used for creating graphical user interfaces (GUI) in Python.

from tkinter import messagebox:
Import messagebox from Tkinter, which provides pop-up dialogs like warnings or info boxes.

def add_task():
Define a function called add_task() to add a task to the to-do list.

task = entry.get()
Get the text from the entry widget (where the user types their task).

if task:
Check if task is not empty (i.e., if the user has entered something).

listbox.insert(tk.END, task)
Insert the task into the listbox widget at the end of the list.

entry.delete(0, tk.END)
Clear the text in the entry widget after adding the task.

else:
If the task is empty, proceed to the next line.

messagebox.showwarning("Warning", "You must enter a task.")
Show a warning message box to the user, indicating that they need to enter a task.

def delete_task():
Define a function called delete_task() to delete the selected task from the to-do list.

try:
Start a try block to handle any errors when deleting a task.

selected_task_index = listbox.curselection()[0]
Get the index of the currently selected task in the listbox.

listbox.delete(selected_task_index)
Delete the task from the listbox using the obtained index.

except:
If an error occurs (e.g., no task is selected), proceed to the next line.

messagebox.showwarning("Warning", "You must select a task to delete.")
Show a warning message box if the user tries to delete a task without selecting one.

def clear_all_tasks():
Define a function called clear_all_tasks() to delete all tasks from the listbox.

listbox.delete(0, tk.END)
Delete all tasks from the listbox, from the first item (0) to the end (tk.END).

root = tk.Tk()
Create the main application window and assign it to root.

root.title("To-Do List Application")
Set the title of the main window to "To-Do List Application".

entry = tk.Entry(root, width=50)
Create an Entry widget to allow the user to type in tasks. Set its width to 50.

add_button = tk.Button(root, text="Add Task", command=add_task)
Create a button labeled "Add Task" that calls add_task() when clicked.

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
Create a button labeled "Delete Task" that calls delete_task() when clicked.

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks)
Create a button labeled "Clear All Tasks" that calls clear_all_tasks() when clicked.

listbox = tk.Listbox(root, width=50, height=10)
Create a Listbox widget to display tasks, with a width of 50 and height of 10 items.

entry.pack(pady=10)
Pack (place) the entry widget in the window with padding (pady=10) on the y-axis.

add_button.pack(pady=5)
Pack the add_button widget in the window with padding (pady=5) on the y-axis.

delete_button.pack(pady=5)
Pack the delete_button widget in the window with padding (pady=5) on the y-axis.

clear_button.pack(pady=5)
Pack the clear_button widget in the window with padding (pady=5) on the y-axis.

listbox.pack(pady=10)
Pack the listbox widget in the window with padding (pady=10) on the y-axis.

root.mainloop()
Start the Tkinter event loop, which keeps the application running and responsive.
'''