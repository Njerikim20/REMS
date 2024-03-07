
from tkinter import*
from dashboard import *
from PIL import Image, ImageTk

root=Tk()
root.title("Real Estates")
root.geometry('900x500+200+100')
root.resizable(False,False)

font_type=('georgia',12)

line=Canvas(root,bg="black", width=500,height=2).place(x=260,y=60)
header=Label(root,text="Real Estate Management System",font=('georgia',16))
header.place(x=300,y=30)

#property

img= Image.open('images/property.png')
resize_img=img.resize((80,80))
propertyimg=ImageTk.PhotoImage(resize_img)
Label(root,image=propertyimg).place(x=300,y=80)

def property_instance():
    prop=property(root)
    

propbtn=Button(root, text="Properties",font=font_type,border=2,fg="brown",command=property_instance).place(x=300,y=170)



#tenants

img= Image.open('images/tenants.png')
resize_img=img.resize((80,80))
tenantimg=ImageTk.PhotoImage(resize_img)
Label(root,image=tenantimg).place(x=480,y=80)

def tenant_instance():
    tena=tenant(root)


tenbtn=Button(root, text="Tenants",font=font_type,border=2,fg="brown",command=tenant_instance).place(x=480,y=170)




#finances

img= Image.open('images/finances.png')
resize_img=img.resize((80,80))
financeimg=ImageTk.PhotoImage(resize_img)
Label(root,image=financeimg).place(x=660,y=80)

def finance_instance():
    fina=finance(root)

finabtn=Button(root, text="Finances",font=font_type,border=2,fg="brown",command=finance_instance).place(x=660,y=170)

#schedule

img= Image.open('images/calendar.png')
resize_img=img.resize((80,80))
scheduleimg=ImageTk.PhotoImage(resize_img)
Label(root,image=scheduleimg).place(x=300,y=250)

def schedule_instance():
    sche=schedule(root)

schedulebtn=Button(root, text="Schedules",font=font_type,border=2,fg="brown",command=schedule_instance).place(x=300,y=340)

#maintenace

img= Image.open('images/maintenance.png')
resize_img=img.resize((80,80))
maintenanceimg=ImageTk.PhotoImage(resize_img)
Label(root,image=maintenanceimg).place(x=480,y=250)

def maintenance_instance():
    mainten=maintenance(root)

maintenbtn=Button(root, text="Maintenances",font=font_type,border=2,fg="brown",command=maintenance_instance).place(x=480,y=340)


#settings

img= Image.open('images/settings.png')
resize_img=img.resize((80,80))
settingsimg=ImageTk.PhotoImage(resize_img)
Label(root,image=settingsimg).place(x=660,y=250)

def settings_instance():
    sett=setting(root)

setbtn=Button(root, text="Settings",font=font_type,border=2,fg="brown",command=settings_instance).place(x=660,y=340)

root.mainloop()
