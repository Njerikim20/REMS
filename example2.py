from tkinter import *

def show_property_details(property_id):
    # Function to show detailed view of a property
    # This could include more information and options for the client
    property_details_window = Toplevel(root)
    property_details_window.title("Property Details")
    property_details_window.geometry("400x300")
    property_details_window.resizable(False, False)

    property_details_label = Label(property_details_window, text=f"Property ID: {property_id}\nProperty Details Here...")
    property_details_label.pack()

def show_properties():
    # Function to show list of properties
    properties_window = Toplevel(root)
    properties_window.title("Properties")
    properties_window.geometry("400x300")
    properties_window.resizable(False, False)

    properties = [
        {"id": 1, "name": "Property 1", "location": "Location 1"},
        {"id": 2, "name": "Property 2", "location": "Location 2"},
        {"id": 3, "name": "Property 3", "location": "Location 3"},
        # Add more properties as needed
    ]

    for property in properties:
        property_frame = Frame(properties_window)
        property_frame.pack(pady=5)

        property_label = Label(property_frame, text=f"{property['name']} - {property['location']}")
        property_label.pack(side=LEFT, padx=10)

        view_button = Button(property_frame, text="View", command=lambda id=property['id']: show_property_details(id))
        view_button.pack(side=RIGHT, padx=10)

# Main Tkinter window
root = Tk()
root.title("Real Estate Management System")
root.geometry("600x400")
root.resizable(False, False)

# Button to open properties interface
properties_button = Button(root, text="View Properties", command=show_properties)
properties_button.pack(pady=50)

root.mainloop()
