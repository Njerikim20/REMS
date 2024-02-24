from tkinter import *
from tkinter import messagebox

class REMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Real Estate Management System")
        self.root.geometry("600x400")

        self.label = Label(root, text="Welcome to REMS", font=("Arial", 20))
        self.label.pack(pady=20)

        self.client_btn = Button(root, text="Client", command=self.client_interface)
        self.client_btn.pack(pady=10)

        self.landlord_btn = Button(root, text="Landlord", command=self.landlord_interface)
        self.landlord_btn.pack(pady=10)

    def client_interface(self):
        self.clear_screen()
        self.label = Label(self.root, text="Client Interface", font=("Arial", 20))
        self.label.pack(pady=20)

        self.property_list_btn = Button(self.root, text="View Properties", command=self.view_properties)
        self.property_list_btn.pack(pady=10)

        self.express_interest_btn = Button(self.root, text="Express Interest", command=self.express_interest)
        self.express_interest_btn.pack(pady=10)

    def view_properties(self):
        # Simulated property listing
        properties = ["Property 1", "Property 2", "Property 3"]
        messagebox.showinfo("Properties", "\n".join(properties))

    def express_interest(self):
        messagebox.showinfo("Express Interest", "Your interest has been sent to the landlord.")

    def landlord_interface(self):
        self.clear_screen()
        self.label = Label(self.root, text="Landlord Interface", font=("Arial", 20))
        self.label.pack(pady=20)

        self.view_interest_btn = Button(self.root, text="View Client's Interest", command=self.view_interest)
        self.view_interest_btn.pack(pady=10)

    def view_interest(self):
        # Simulated client's interest
        interest = ["Client 1 - Property 2", "Client 2 - Property 3"]
        messagebox.showinfo("Client's Interest", "\n".join(interest))

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    app = REMS(root)
    root.mainloop()
