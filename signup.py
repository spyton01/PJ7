import sqlite3

# Connect to the database
connect = sqlite3.connect('UserLogData.db')
cursor = connect.cursor()

# Create Users table if it does not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Users
               (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)''')

# Commit changes and close connection
connect.commit()
connect.close()

from tkinter import *
import sqlite3

def sign_up():
    # Get user inputs
    name_text = name.get()
    email_text = email.get()
    password_text = password.get()
    confirm_password_text = confirm_password.get()
    
    # Validate email format
    if "@" not in email_text or "." not in email_text:
        error_label.config(text="Invalid email format")
        return
    
    # Validate passwords match
    if password_text != confirm_password_text:
        error_label.config(text="Passwords do not match")
        return
    
    # Connect to the database
    connect = sqlite3.connect('UserLogData.db')
    cursor = connect.cursor()
    
    # Insert user information into the appropriate table
    cursor.execute("INSERT INTO Users (name, email, password) VALUES (?, ?, ?)", (name_text, email_text, password_text))
    
    # Commit changes and close connection
    connect.commit()
    connect.close()
    
    # Display success message
    error_label.config(text="User signed up successfully!", fg="green")

root = Tk()
root.title("Sign Up")
root.geometry('400x200')

name = StringVar()
email = StringVar()
password = StringVar()
confirm_password = StringVar()

name_label = Label(root, text='Name', font=('Candara', 12))
name_entry = Entry(root, textvariable=name, font=('Candara', 12))

email_label = Label(root, text='Email', font=('Candara', 12))
email_entry = Entry(root, textvariable=email, font=('Candara', 12))

password_label = Label(root, text='Password', font=('Candara', 12))
password_entry = Entry(root, textvariable=password, show='*', font=('Candara', 12))

confirm_password_label = Label(root, text='Confirm Password', font=('Candara', 12))
confirm_password_entry = Entry(root, textvariable=confirm_password, show='*', font=('Candara', 12))

sub_btn = Button(root, text='Sign up Now', font=('Candara'), command=sign_up)
error_label = Label(root, text='', fg='red')

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)

password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)

confirm_password_label.grid(row=3, column=0)
confirm_password_entry.grid(row=3, column=1)

sub_btn.grid(row=4, columnspan=2)
error_label.grid(row=5, columnspan=2)

root.mainloop()