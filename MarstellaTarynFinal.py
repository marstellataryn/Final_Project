import tkinter as tk
from tkinter import messagebox

class PhonebookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Facility Contact Info")

        # Variables to store user inputs
        self.facility_name_var = tk.StringVar()
        self.city_var = tk.StringVar()
        self.fax_var = tk.StringVar()
        self.phone_var = tk.StringVar()

        # load images
        self.add_icon = self.resize_image(tk.PhotoImage(file="entersign.png"), 25, 25)
        self.exit_icon = self.resize_image(tk.PhotoImage(file="exitsign.png"), 25, 25)
        # list to save entries
        self.entries = []

        # Create main window widgets
        self.create_widgets()

    def create_widgets(self):
        # Create label
        self.master.configure(bg="black")
        tk.Label(self.master, text="Facility Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.master, text="City:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.master, text="Fax Number:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.master, text="Phone Number:").grid(row=3, column=0, padx=10, pady=10, sticky="e")

        # Create entry widgets
        label_options = {'bg': 'black', 'fg': 'red', 'padx': 10, 'pady': 10, 'sticky': 'e'}
        tk.Entry(self.master, textvariable=self.facility_name_var).grid(row=0, column=1, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.city_var).grid(row=1, column=1, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.fax_var).grid(row=2, column=1, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.phone_var).grid(row=3, column=1, padx=10, pady=10)

        # Create buttons with images
        
        tk.Button(self.master, text="Add Entry", command=self.add_entry,image=self.add_icon, compound="left").grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Show Entries", command=self.show_entries).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.master, command=self.master.destroy, image=self.exit_icon, compound="left").grid(row=6, column=0, columnspan=2, pady=10)

    def add_entry(self):
        # Callback function for "Add Entry" button
        facility_name = self.facility_name_var.get()
        city = self.city_var.get()
        fax = self.fax_var.get()
        phone = self.phone_var.get()

        # Perform input validation
        if not all([facility_name, city, fax, phone]):
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return

        entry = {
            "Facility Name": facility_name,
            "City": city,
            "Fax Number": fax,
            "Phone Number": phone
            }
        self.entries.append(entry)

        self.sort_entries()

        self.print_entries()


        # Clear the entry fields
        self.facility_name_var.set("")
        self.city_var.set("")
        self.fax_var.set("")
        self.phone_var.set("")

    def sort_entries(self):
        self.entries.sort(key=lambda x: x["Facility Name"].lower())

    def print_entries(self):
        if not self.entries:
            print("No entries to display.")
            return

        header = ["Facility Name", "City", "Fax Number", "Phone Number"]
        print("{:<20} {:<20} {:<20} {:<20}".format(*header))
        print("=" * 80)
        for entry in self.entries:
            row = [entry["Facility Name"], entry["City"], entry["Fax Number"], entry["Phone Number"]]
            print("{:<20} {:<20} {:<20} {:<20}".format(*row))
    def show_entries(self):
        # Callback function for "Show Entries" button
        self.print_entries()


    def resize_image(self, image, width, height):
        return image.subsample(int(image.width() / width), int(image.height() / height))
def main():
    
    root = tk.Tk()
    app = PhonebookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
