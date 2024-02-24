from tkinter import *

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Create the main window
root = Tk()
root.title("Real Estate Management System")
root.geometry("800x600")

# Create a dictionary to store frames
frames = {}

# Create the main dashboard frame
dashboard_frame = Frame(root)
dashboard_frame.pack(fill="both", expand=True)
frames["dashboard"] = dashboard_frame

# Create buttons to switch to different interfaces
tenant_button = Button(dashboard_frame, text="Tenants", command=lambda: show_frame(frames["tenants"]))
tenant_button.pack()
landlord_button = Button(dashboard_frame, text="Landlords", command=lambda: show_frame(frames["landlords"]))
landlord_button.pack()

# Create the tenants interface
tenants_frame = Frame(root)
tenants_frame.pack(fill="both", expand=True)
frames["tenants"] = tenants_frame

# Create buttons and functionality for tenants interface
all_properties_button = Button(tenants_frame, text="All Properties")
all_properties_button.pack()
my_properties_button = Button(tenants_frame, text="My Properties")
my_properties_button.pack()
payments_button = Button(tenants_frame, text="Payments")
payments_button.pack()
maintenance_request_button = Button(tenants_frame, text="Maintenance Request")
maintenance_request_button.pack()

# Create the landlords interface
landlords_frame = Frame(root)
landlords_frame.pack(fill="both", expand=True)
frames["landlords"] = landlords_frame

# Create buttons and functionality for landlords interface
all_clients_button = Button(landlords_frame, text="All Clients")
all_clients_button.pack()
payments_button = Button(landlords_frame, text="Payments")
payments_button.pack()
maintenance_requests_button = Button(landlords_frame, text="Maintenance Requests")
maintenance_requests_button.pack()

# Show the main dashboard frame initially
show_frame(dashboard_frame)

# Run the tkinter event loop
root.mainloop()
