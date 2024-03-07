from tkinter import *
from tkinter import ttk, simpledialog, messagebox
import sqlite3

import hashlib
import subprocess

root=Tk()
root.title('login')
root.geometry('925x500+100+100')
root.configure(bg="#fff")
root.resizable(False,False)

class Login:
    def __init__(self, root):
        self.root = root

        self.connection = sqlite3.connect("Real Estate.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS login (
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) UNIQUE,
                password VARCHAR(255)
            )
        """)
        self.connection.commit()

        self.img = PhotoImage(file='pics/logo2.png')
        Label(root, image=self.img, bg='white', width=300, height=300 ).place(x=100, y=50)
        self.login_frame = LabelFrame(root, bg="#8d5524", width=350, border=0, height=500, padx=20, pady=30)
        self.login_frame.place(x=480, y=100)


        username_label = Label(self.login_frame, text="Username", bg="#8d5524")
        username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = Label(self.login_frame, text="Password", bg="#8d5524")
        password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_btn = Button(self.login_frame, text="Login", bg="gold", command=self.login)
        self.login_btn.grid(row=2, column=1, padx=10, pady=15)

        self.creation_label = Label(self.login_frame, text="Don't have an account?", bg="#8d5524")
        self.creation_label.grid(row=3, column=0, columnspan=2, padx=10, pady=18)
        self.signup_btn = Button(self.login_frame, text="Signup", bg="gold", command=self.open_signup_interface)
        self.signup_btn.grid(row=3, column=2, padx=10, pady=18)


    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username exists
        self.cursor.execute("SELECT * FROM login WHERE username = ?", (username,))
        user_record = self.cursor.fetchone()

        if user_record:
            stored_password = user_record[2]  # Assuming password is in the third column
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            if stored_password == hashed_password:
                messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
                self.root.destroy()  # Close the login window
                subprocess.run(["python", "main.py"])  # Open the main.py filer
            else:
                messagebox.showerror("Login Failed", "Invalid password")
        else:
            messagebox.showerror("Login Failed", "Invalid username")

    def open_signup_interface(self):
        # Open the sign_up.py file
        subprocess.run(["python", "signup.py"])

app = Login(root)
root.mainloop()



