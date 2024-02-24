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

class login:
    def __init__(self,root):
        
        self.root = root
        root.title("Login Interface")

        self.connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="root",
                    database="REMS"
                )
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS login (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE,
                password VARCHAR(255)
            )
        """)
        self.connection.commit()
img= PhotoImage(file='pics/logo2.png')
Label(root,image=img,bg='white', width=300, height=300 ).place(x=100,y=50)
login= LabelFrame(root,bg="#8d5524",width=350,border=0, height=400,padx=20,pady=30).place(x=480,y=70,rely=0.0)

username=Label(login,text="Username",bg="#8d5524").place(x=550,y=150)
userfield=Entry(login).place(x=630,y=150)

password=Label(login, text="Password", bg="#8d5524").place(x=550,y=200)
passfield=Entry(login,show="*").place(x=630, y=200)

loginbtn=Button(login, text="Login", bg="gold",command=login).place(x=630,y=250)

creation=Label(login,text="Don't have an account?", bg="#8d5524").place(x=550,y=350)
signupbtn=Button(login, text="Signup", bg="gold",command=open_signup).place(x=690,y=350)

def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username exists
        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_record = self.cursor.fetchone()

        if user_record:
            stored_password = user_record[2]  # Assuming password is in the third column
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            if stored_password == hashed_password:
                messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
                self.root.destroy()  # Close the login window
                subprocess.run(["python", "software.py"])  # Open the software.py file
            else:
                messagebox.showerror("Login Failed", "Invalid password")
        else:
            messagebox.showerror("Login Failed", "Invalid username")

def open_signup_interface(self):
        # Open the sign_up.py file
        subprocess.run(["python", "sign_up.py"])


root.mainloop()


