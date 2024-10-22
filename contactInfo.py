import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Contact Manager")
root.geometry("400x500")

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get("1.0", "end-1c")
    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields!")

def view_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['Phone']}")

def update_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    name = selected_contact.split(" - ")[0]
    if name in contacts:
        contacts[name] = {'Phone': phone_entry.get(), 'Email': email_entry.get(), 'Address': address_entry.get("1.0", "end-1c")}
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()

def search_contact():
    search_name = search_entry.get()
    if search_name in contacts:
        details = contacts[search_name]
        messagebox.showinfo("Contact Found", f"Name: {search_name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
    else:
        messagebox.showerror("Error", "Contact not found!")

def delete_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    name = selected_contact.split(" - ")[0]
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        view_contacts()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Text(root, height=4, width=30)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack()
tk.Button(root, text="Update Contact", command=update_contact).pack()
tk.Button(root, text="Search Contact", command=search_contact).pack()

contact_list = tk.Listbox(root)
contact_list.pack()

tk.Button(root, text="View Contacts", command=view_contacts).pack()
tk.Button(root, text="Delete Contact", command=delete_contact).pack()

tk.Label(root, text="Search by Name").pack()
search_entry = tk.Entry(root)
search_entry.pack()

root.mainloop()


'''
Here's a breakdown of each line of the code, explaining how the contact management system works:

import tkinter as tk: This imports the Tkinter library to create the graphical user interface (GUI).

from tkinter import messagebox: This imports the messagebox module from Tkinter, 
which is used to display pop-up dialogs like alerts, errors, and information.

root = tk.Tk(): This initializes the main application window (called root).

root.title("Contact Manager"): This sets the title of the application window to "Contact Manager."

root.geometry("400x500"): This sets the size of the window to 400x500 pixels.

contacts = {}: This creates an empty dictionary contacts where the contact information (name, phone, email, and address) will be stored.

Functions:
def add_contact():: This function handles adding a new contact to the contacts dictionary.

name = name_entry.get(): Retrieves the text entered in the name_entry input field.

phone = phone_entry.get(): Retrieves the phone number entered in the phone_entry input field.

email = email_entry.get(): Retrieves the email entered in the email_entry input field.

address = address_entry.get("1.0", "end-1c"): Retrieves the address entered in the address_entry text box. 
"1.0" specifies the first character, and "end-1c" excludes the trailing newline character.

if name and phone:: This checks if the name and phone fields are filled in, as these are required fields for adding a contact.

contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}: If the required fields are filled, 
this adds a new contact to the contacts dictionary. The contact is stored as a dictionary with 'Phone', 'Email', and 'Address' fields.

messagebox.showinfo("Success", "Contact added successfully!"): Displays a success message box indicating that the contact was added.

clear_entries(): Calls the clear_entries() function to clear the input fields after adding a contact.

else:: If the name or phone fields are empty, it will execute the following block.

messagebox.showerror("Error", "Name and Phone are required fields!"): Displays an error message box if the required fields are not filled.

def view_contacts():: This function is responsible for displaying all the contacts in the list.

contact_list.delete(0, tk.END): Clears the current list of contacts displayed in the listbox widget.

for name, details in contacts.items():: Loops through the contacts dictionary to display each contact's name and phone number.

contact_list.insert(tk.END, f"{name} - {details['Phone']}"): Inserts the contact's name and phone number into the listbox widget.

def update_contact():: This function updates the selected contact’s details.

selected_contact = contact_list.get(contact_list.curselection()): Retrieves the selected contact from the listbox.

name = selected_contact.split(" - ")[0]: Extracts the name of the selected contact from the listbox entry (which contains both name and phone).

if name in contacts:: Checks if the selected contact’s name exists in the contacts dictionary.

contacts[name] = {'Phone': phone_entry.get(), 'Email': email_entry.get(), 'Address': 
address_entry.get("1.0", "end-1c")}: Updates the contact's information in the contacts dictionary with the new values from the entry fields.

messagebox.showinfo("Success", "Contact updated successfully!"): Displays a success message box after the contact is updated.

clear_entries(): Clears the input fields after the contact is updated.

def search_contact():: This function searches for a contact by name.

search_name = search_entry.get(): Retrieves the text entered in the search entry field.

if search_name in contacts:: Checks if the search name exists in the contacts dictionary.

details = contacts[search_name]: If found, retrieves the contact details.

messagebox.showinfo("Contact Found", f"Name: {search_name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: 
{details['Address']}"): Displays the contact's details in a pop-up message box.

else:: If the contact is not found, the following block is executed.

messagebox.showerror("Error", "Contact not found!"): Displays an error message if the contact is not found.

def delete_contact():: This function deletes the selected contact.

selected_contact = contact_list.get(contact_list.curselection()): Retrieves the selected contact from the listbox.

name = selected_contact.split(" - ")[0]: Extracts the name of the selected contact.

if name in contacts:: Checks if the selected contact exists in the contacts dictionary.

del contacts[name]: Deletes the contact from the contacts dictionary.

messagebox.showinfo("Success", "Contact deleted successfully!"): Displays a success message box after the contact is deleted.

view_contacts(): Refreshes the contact list to reflect the deletion.

def clear_entries():: This function clears all the input fields.

name_entry.delete(0, tk.END): Clears the name_entry field.

phone_entry.delete(0, tk.END): Clears the phone_entry field.

email_entry.delete(0, tk.END): Clears the email_entry field.

address_entry.delete("1.0", tk.END): Clears the address_entry text box.

GUI Setup:
tk.Label(root, text="Name").pack(): Creates and packs a label for the name field.

name_entry = tk.Entry(root): Creates an entry widget for the name input.

name_entry.pack(): Packs the name entry widget into the window.

tk.Label(root, text="Phone").pack(): Creates and packs a label for the phone field.

phone_entry = tk.Entry(root): Creates an entry widget for the phone input.

phone_entry.pack(): Packs the phone entry widget into the window.

tk.Label(root, text="Email").pack(): Creates and packs a label for the email field.

email_entry = tk.Entry(root): Creates an entry widget for the email input.

email_entry.pack(): Packs the email entry widget into the window.

tk.Label(root, text="Address").pack(): Creates and packs a label for the address field.

address_entry = tk.Text(root, height=4, width=30): Creates a text box for the address input.

address_entry.pack(): Packs the address text box into the window.

tk.Button(root, text="Add Contact", command=add_contact).pack(): Creates a button to add a contact and binds it to the add_contact function.

tk.Button(root, text="Update Contact", command=update_contact).pack(): 
Creates a button to update a contact and binds it to the update_contact function.

tk.Button(root, text="Search Contact", command=search_contact).pack(): 
Creates a button to search for a contact and binds it to the search_contact function.

contact_list = tk.Listbox(root): Creates a listbox widget to display the list of contacts.

contact_list.pack(): Packs the listbox widget into the window.

tk.Button(root, text="View Contacts", command=view_contacts).pack(): 
Creates a button to view all contacts and binds it to the view_contacts function.

tk.Button(root, text="Delete Contact", command=delete_contact).pack(): 
Creates a button to delete a contact and binds it to the delete_contact function.

tk.Label(root, text="Search by Name").pack(): Creates and packs a label for the search field.

search_entry = tk.Entry(root): Creates an entry widget for searching contacts by name.

search_entry.pack(): Packs the search entry widget into the window.

root.mainloop(): This starts the Tkinter event loop, keeping the window open and interactive until it is closed.
'''