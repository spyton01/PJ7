from tkinter import *
import sqlite3

def sign_in():
    # Get user inputs
    email_text = email.get()
    password_text = password.get()
    
    # Connect to the database
    connect = sqlite3.connect('UserLogData.db')
    cursor = connect.cursor()
    
    # Check if user exists in the database
    cursor.execute("SELECT * FROM Users WHERE email=? AND password=?", (email_text, password_text))
    user = cursor.fetchone()
    
    if user:
        sign_in_label.config(text="Login successful", fg="green")
    else:
        sign_in_label.config(text="Email or password incorrect", fg="red")
    
    # Close connection
    connect.close()

root = Tk()
root.title("Sign In")
root.geometry('300x150')

email = StringVar()
password = StringVar()

email_label = Label(root, text='Email', font=('Candara', 12))
email_entry = Entry(root, textvariable=email, font=('Candara', 12))

password_label = Label(root, text='Password', font=('Candara', 12))
password_entry = Entry(root, textvariable=password, show='*', font=('Candara', 12))

sign_in_btn = Button(root, text='Sign In', command=sign_in, font=('Candara', 12))
sign_in_label = Label(root, text='', font=('Candara', 12))

email_label.grid(row=0, column=0)
email_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

sign_in_btn.grid(row=2, columnspan=2)
sign_in_label.grid(row=3, columnspan=2)

root.mainloop()