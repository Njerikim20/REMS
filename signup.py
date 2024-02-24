from tkinter import *
from tkinter import messagebox 
import re

root=Tk()
root.title('signup')
root.geometry('925x500+100+100')
root.configure(bg="#fff")
root.resizable(False,False)

img= PhotoImage(file='pics/logo2.png')
Label(root,image=img,bg='white', width=200, height=200 ).place(x=50,y=50)

signup= LabelFrame(root,bg="#8d5524",width=350,border=0, height=400,padx=20,pady=30).place(x=480,y=70,rely=0.0)

email=Label(signup,text="Email Address",bg="#8d5524").place(x=550,y=100)
emailfield=Entry(signup).place(x=655,y=100)

username=Label(signup,text="Username",bg="#8d5524").place(x=550,y=150)
userfield=Entry(signup).place(x=655,y=150)

name=Label(signup,text="Client Name",bg="#8d5524").place(x=550,y=200)
fnamefield=Entry(signup).place(x=655,y=200)

phone_number=Label(signup,text="Phone Number",bg="#8d5524").place(x=550,y=250)
contactfield=Entry(signup).place(x=655,y=250)

#def validate_phone_number(phone_number):
 #   pattern = r'^\d{10}$'
  #  if re.match(pattern, phone_number):
   #     return True
    #else:
     #   return False

password=Label(signup, text="Password", bg="#8d5524").place(x=550,y=300)
passfield=Entry(signup,show="*").place(x=655, y=300)

confirmpass=Label(signup, text=" Confirm Password", bg="#8d5524").place(x=550,y=350)
confirmpassfield=Entry(signup,show="*").place(x=655, y=350)

registerbtn=Button(signup, text="Register", bg="gold").place(x=655,y=390)

creation=Label(signup,text="Already have an account?", bg="#8d5524").place(x=550,y=430)
loginbtn=Button(signup, text="Login", bg="gold").place(x=690,y=430)

root.mainloop()
