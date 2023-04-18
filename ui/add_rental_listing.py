import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from const import LARGEFONT, bedrooms, locations


class AddRentalListing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #navigation
        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame("Homepage"))
        button1.grid(row=0, column=1, padx=10, pady=10)
        button2 = ttk.Button(self, text="Rental Listings",
                             command=lambda: controller.show_frame("RentalListings"))
        button2.grid(row=0, column=2, padx=10, pady=10)
        button3 = ttk.Button(self, text="Request new listing",
                             command=lambda: controller.show_frame("RequestRental"))
        button3.grid(row=0, column=3, padx=10, pady=10)
        button4 = ttk.Button(self, text="Available agents",
                             command=lambda: controller.show_frame("ListOfAvailableAgents"))
        button4.grid(row=0, column=4, padx=10, pady=10)
        button5 = ttk.Button(self, text="Account",
                             command=lambda: controller.show_frame("UserProfile"))
        button5.grid(row=0, column=5, padx=10, pady=10)

        # Left side - Current listed properties
        label = ttk.Label(self, text="Add Rental Listing", font=LARGEFONT)
        label.grid(row=1, column=0, padx=10, pady=10)
        self.selected_location = tk.StringVar(value="Kapsabet")
        self.selected_bedroom = tk.StringVar(value="1")

        # Right side - Form to upload new rental

        # Create labels and entry fields for each input
        # property_type_label = tk.Label(self, text="Property Type:")
        # self.property_type_entry = tk.Entry(self)

        num_bedrooms_label = tk.Label(self, text="Number of Bedrooms:")
        bedrooms_dropdown = ttk.OptionMenu(self, self.selected_bedroom, *bedrooms)

        # num_bathrooms_label = tk.Label(self, text="Number of Bathrooms:")
        # self.num_bathrooms_entry = tk.Entry(self)

        rental_price_label = tk.Label(self, text="Rental Price:")
        self.rental_price_entry = tk.Entry(self)

        location_label = tk.Label(self, text="Location:")
        locations_button = ttk.OptionMenu(self, self.selected_location, *locations)

        description_label = tk.Label(self, text="Description:")
        self.description_entry = tk.Entry(self)

        # Add a submit button to save the input
        submit_button = tk.Button(self, text="Submit", command=self.submit)

        # Use grid layout to arrange the labels and entry fields
        # property_type_label.grid(row=2, column=1, padx=5, pady=5)
        # self.property_type_entry.grid(row=2, column=2, padx=5, pady=5)

        num_bedrooms_label.grid(row=3, column=1, padx=5, pady=5)
        bedrooms_dropdown.grid(row=3, column=2, padx=5, pady=5)

        # num_bathrooms_label.grid(row=4, column=1, padx=5, pady=5)
        # self.num_bathrooms_entry.grid(row=4, column=2, padx=5, pady=5)

        rental_price_label.grid(row=5, column=1, padx=5, pady=5)
        self.rental_price_entry.grid(row=5, column=2, padx=5, pady=5)

        location_label.grid(row=6, column=1, padx=5, pady=5)
        locations_button.grid(row=6, column=2, padx=5, pady=5)

        description_label.grid(row=7, column=1, padx=5, pady=5)
        self.description_entry.grid(row=7, column=2, padx=5, pady=5)

        submit_button.grid(row=8, column=2, padx=5, pady=5)

        # Store the controller object so we can access it later
        self.controller = controller

    def submit(self):
        # Retrieve the input from the entry fields
        property_type = self.property_type_entry.get()
        num_bedrooms = self.num_bedrooms_entry.get()
        num_bathrooms = self.num_bathrooms_entry.get()
        rental_price = self.rental_price_entry.get()
        location = self.location_entry.get()
        description = self.description_entry.get()

        # Do any necessary validation of the input here

        # Save the input to a database or file
        # (This is just a placeholder; replace with your own code)
        with open("rentals.txt", "a") as f:
            f.write(
                f"{property_type}, {num_bedrooms}, {num_bathrooms}, {rental_price}, {location}, {description}\n")

        # Display a success message to the user
        messagebox.showinfo("Success", "Rental listing added!")

        # Clear the entry fields






