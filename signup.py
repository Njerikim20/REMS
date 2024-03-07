from tkinter import *
from tkinter import messagebox 
import sqlite3
import hashlib
import subprocess

root = Tk()
root.title('Signup')
root.geometry('925x500+100+100')
root.configure(bg="#fff")
root.resizable(False, False)

class Signup:
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
        Label(root, image=self.img, bg='white', width=200, height=200).place(x=100,y=70)

        self.signup_frame = LabelFrame(root, bg="#8d5524", width=350, border=0, height=400, padx=20, pady=30)
        self.signup_frame.place(x=480,y=70)

        Label(self.signup_frame, text="Email Address", bg="#8d5524").grid(row=0, column=0,pady=2)
        self.email_field = Entry(self.signup_frame)
        self.email_field.grid(row=0, column=1,pady=2)

        Label(self.signup_frame, text="Username", bg="#8d5524").grid(row=1, column=0,pady=4)
        self.username_field = Entry(self.signup_frame)
        self.username_field.grid(row=1, column=1,pady=4)

        Label(self.signup_frame, text="Client Name", bg="#8d5524").grid(row=2, column=0,pady=5)
        self.fname_field = Entry(self.signup_frame)
        self.fname_field.grid(row=2, column=1,pady=5)

        Label(self.signup_frame, text="Phone Number", bg="#8d5524").grid(row=3, column=0,pady=6)
        self.contact_field = Entry(self.signup_frame)
        self.contact_field.grid(row=3, column=1,pady=6)

        Label(self.signup_frame, text="Password", bg="#8d5524").grid(row=4, column=0,pady=7)
        self.pass_field = Entry(self.signup_frame, show="*")
        self.pass_field.grid(row=4, column=1,pady=7)

        Label(self.signup_frame, text="Confirm Password", bg="#8d5524").grid(row=5, column=0,pady=8)
        self.confirmpass_field = Entry(self.signup_frame, show="*")
        self.confirmpass_field.grid(row=5, column=1,pady=8)

        self.register_btn = Button(self.signup_frame, text="Register", bg="gold", command=self.save_and_open_login)
        self.register_btn.grid(row=6, column=0, columnspan=2,pady=15)

        Label(self.signup_frame, text="Already have an account?", bg="#8d5524").grid(row=7, column=0,pady=18)
        login_btn = Button(self.signup_frame, text="Login", bg="gold")
        login_btn.grid(row=7, column=1,pady=18)

    def save_and_open_login(self):
        username = self.username_field.get()
        password = self.pass_field.get()

        # Hash the password before storing it in the database
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if the username already exists
        self.cursor.execute("SELECT * FROM login WHERE username = ?", (username,))

        existing_user = self.cursor.fetchone()

        if existing_user:
            messagebox.showerror("Sign Up Failed", "Username already exists")
        else:
            # Insert the new user into the database
            self.cursor.execute("INSERT INTO login (username, password) VALUES (?, ?)", (username, hashed_password))
            self.connection.commit()
            messagebox.showinfo("Sign Up Successful", "User created successfully")
            self.root.destroy()  # Close the signup window

            # Open the login.py file
            subprocess.run(["python", "login.py"])

app = Signup(root)
root.mainloop()




