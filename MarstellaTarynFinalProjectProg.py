# Taryn Marstella
# SDEV Final Project
# Facility Contact Info APP
# Python Idle

import tkinter as tk

class FacilityBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Facility Contact Info App")

        self.facility_book = {}

        # create labels
        self.label_facility = tk.Label(root,text="Facility Name:")
        self.label_address = tk.Label(root, text="Address:")
        self.label_phone = tk.Label(root, text="Phone Number:")
        self.label_fax = tk.Label(root, text="Fax Number:")

        # entry widgets
        self.entry_facility = tk.Entry(root)
        self.entry_address = tk.Entry(root)
        self.entry_phone = tk.Entry(root)
        self.entry_fax = tk.Entry(root)

        self.add_button = tk.Button(root, text="Add Facility", command=self.add_facility)

        # book access button
        self.facility_listbox = tl.Listbox(root, width=50)
        self.facility_listbox.grid(row=5, column=0, columnspan=2, pady=10)

        
                                        

        
