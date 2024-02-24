from tkinter import *

blue="#ADD8E6"
class property:
    def __init__(self,root):
        
            
            
            properties=Frame(root,bg=blue, width=500,height=400)
            properties.place(x=260,y=75)

            def destroy_property():
                  properties.destroy()
           
            backbtn=Button(properties,text="back", bg="silver",command=destroy_property).place(x=20,y=15)

class tenant:
    def __init__(self,root):
        
            tenants=Frame(root,bg=blue, width=500,height=400)
            tenants.place(x=260,y=75)

            def destroy_tenant():
                  tenants.destroy()

            backbtn=Button(tenants,text="back", bg="silver",command=destroy_tenant).place(x=20,y=15)

    

class finance:
    def __init__(self,root):
            
            finances=Frame(root,bg=blue, width=500,height=400)
            finances.place(x=260,y=75)

            def destroy_finance():
                  finances.destroy()
           
            backbtn=Button(finances,text="back", bg="silver",command=destroy_finance).place(x=20,y=15)    
            
class schedule:
    def __init__(self,root):
        
        
            schedules=Frame(root,bg=blue, width=500,height=400)
            schedules.place(x=260,y=75)

            def destroy_schedule():
                  schedules.destroy()
           
            backbtn=Button(schedules,text="back", bg="silver",command=destroy_schedule).place(x=20,y=15)
            
class maintenance:
    def __init__(self,root):
        
        
            maintenances=Frame(root,bg=blue, width=500,height=400)
            maintenances.place(x=260,y=75)
            
            def destroy_maintenance():
                  maintenances.destroy()
           
            backbtn=Button(maintenances,text="back", bg="silver",command=destroy_maintenance).place(x=20,y=15)

class setting:
    def __init__(self,root):
        
        
            settings=Frame(root,bg=blue, width=500,height=400)
            settings.place(x=260,y=75)

            def destroy_setting():
                  settings.destroy()
           
            backbtn=Button(settings,text="back", bg="silver",command=destroy_setting).place(x=20,y=15)