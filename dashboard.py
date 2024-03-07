from tkinter import *
import sqlite3
from tkinter import ttk, simpledialog, messagebox
blue="#ADD8E6"
import sqlite3
from tkinter import *

class property:
    def __init__(self, root):
        self.root = root
        self.blue = "#0000ff"  # Assuming blue is defined somewhere
        con = sqlite3.connect("Real Estate.db")
        self.cursor = con.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                property_id INT PRIMARY KEY,
                property_name VARCHAR(255),
                property_location VARCHAR(255),
                property_price VARCHAR(255),
                property_status VARCHAR(255)
            )
        """)
        con.commit()

        self.properties_frame = Frame(root, bg=self.blue, width=500, height=400)
        self.properties_frame.place(x=260, y=75)

        view_properties_btn = Button(self.properties_frame, text="View Properties", bg="silver", command=self.display_properties)
        view_properties_btn.place(x=60, y=15)

        add_property_btn = Button(self.properties_frame, text="Add Property", bg="silver", command=self.insert_property)
        add_property_btn.place(x=180, y=15)

        edit_property_btn = Button(self.properties_frame, text="Edit Property", bg="silver", command=self.edit_property)
        edit_property_btn.place(x=280, y=15)      
        
        back_btn = Button(self.properties_frame, text="Back", bg="silver", command=self.destroy_property)
        back_btn.place(x=20, y=15)

    def destroy_property(self):
        self.properties_frame.destroy()

    def display_properties(self):
        self.cursor.execute("SELECT * FROM properties")
        properties = self.cursor.fetchall()
        canvas = Canvas(self.root)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        for i, prop in enumerate(properties):
            property_id = prop[0]
            label_text = f"ID: {property_id}, Name: {prop[1]}, Location: {prop[2]}, Price: {prop[3]}"
            label = Label(frame, text=label_text, cursor="hand2")
            label.grid(row=i, column=0, padx=5, pady=5, sticky=W)
            label.bind("<Button-1>", lambda e, id=property_id: self.on_property_click(id))

    
    def on_property_click(self, property_id):
        # Fetch property details from the database based on property_id
        self.cursor.execute("SELECT * FROM properties WHERE property_id = ?", (property_id,))
        property_details = self.cursor.fetchone()

        # Create a new frame to display property details
        property_details_frame = Frame(self.root, bg="white", width=400, height=300)
        property_details_frame.place(x=200, y=200)

        # Display property details in the new frame
        Label(property_details_frame, text=f"Property ID: {property_details[0]}").pack()
        Label(property_details_frame, text=f"Name: {property_details[1]}").pack()
        Label(property_details_frame, text=f"Location: {property_details[2]}").pack()
        Label(property_details_frame, text=f"Price: {property_details[3]}").pack()
        Label(property_details_frame, text=f"Status: {property_details[4]}").pack()

    def insert_property(self):
    # Create a new window for the property form
        property_form_window = Toplevel(self.root)
        property_form_window.title("Add Property")

        # Define and place labels and entry fields for property details
        Label(property_form_window, text="Property ID:").grid(row=0, column=0)
        property_id_entry = Entry(property_form_window)
        property_id_entry.grid(row=0, column=1)

        Label(property_form_window, text="Property Name:").grid(row=1, column=0)
        property_name_entry = Entry(property_form_window)
        property_name_entry.grid(row=1, column=1)

        Label(property_form_window, text="Property Location:").grid(row=2, column=0)
        property_location_entry = Entry(property_form_window)
        property_location_entry.grid(row=2, column=1)

        Label(property_form_window, text="Property Price:").grid(row=3, column=0)
        property_price_entry = Entry(property_form_window)
        property_price_entry.grid(row=3, column=1)

        def add_property_to_db():
        # Get property details from the entry fields
          con = sqlite3.connect("Real Estate.db")
          cursor = con.cursor()
          property_id = property_id_entry.get()
          property_name = property_name_entry.get()
          property_location = property_location_entry.get()
          property_price = property_price_entry.get()

        # Check if property ID already exists in the database
          self.cursor.execute("SELECT * FROM properties WHERE property_id = ?", (property_id,))
          existing_property = self.cursor.fetchone()
          if existing_property:
            messagebox.showerror("Error", "Property ID already exists")
          else:
            # Insert property details into the database
            self.cursor.execute("INSERT INTO properties (property_id, property_name, property_location, property_price, property_status) VALUES (?, ?, ?, ?, ?)", (property_id, property_name, property_location, property_price, "Available"))
            messagebox.showinfo("Success", "Property added successfully")
            # Commit the changes to the database
            self.con.commit()
            # Close the property form window
            

    # Add a button to submit the property details
        add_property_btn = Button(property_form_window, text="Add Property", command=add_property_to_db)
        add_property_btn.grid(row=4, columnspan=2)


    def edit_property(self, property_id):
        property_details = self.cursor.execute("SELECT * FROM properties WHERE property_id = ?", (property_id,)).fetchone()

        self.edit_window = Toplevel(self.root)
        self.edit_window.title("Edit Property")
        self.edit_window.geometry("400x300")

        Label(self.edit_window, text="Property ID:").pack()
        self.edit_property_id = Entry(self.edit_window, width=30)
        self.edit_property_id.insert(0, property_details[0])
        self.edit_property_id.pack()

        Label(self.edit_window, text="Property Name:").pack()
        self.edit_property_name = Entry(self.edit_window, width=30)
        self.edit_property_name.insert(0, property_details[1])
        self.edit_property_name.pack()

        Label(self.edit_window, text="Property Location:").pack()
        self.edit_property_location = Entry(self.edit_window, width=30)
        self.edit_property_location.insert(0, property_details[2])
        self.edit_property_location.pack()

        Label(self.edit_window, text="Property Price:").pack()
        self.edit_property_price = Entry(self.edit_window, width=30)
        self.edit_property_price.insert(0, property_details[3])
        self.edit_property_price.pack()

        save_button = Button(self.edit_window, text="Save", command=lambda: self.save_property(property_id))
        save_button.pack()

    def save_property(self, property_id):
        property_name = self.edit_property_name.get()
        property_location = self.edit_property_location.get()
        property_price = self.edit_property_price.get()

        self.cursor.execute("UPDATE properties SET property_name = ?, property_location = ?, property_price = ? WHERE property_id = ?", (property_name, property_location, property_price, property_id))
        self.con.commit()

        messagebox.showinfo("Success", "Property details updated successfully")
        self.edit_window.destroy()


    
 

class tenant:
    def __init__(self,root):
            self.root=root
            con= sqlite3.connect("Real Estate.db")
            c=con.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS tenants (
                client_username PRIMARY KEY,
                client_name VARCHAR(255) ,
                client_payments VARCHAR(255),
                property_id VARCHAR(255),
                property_name VARCHAR(255)
                )
                     """)
           
            con.commit()
            con.close()
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