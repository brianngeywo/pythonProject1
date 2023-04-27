import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import pymysql

from const import LARGEFONT, bedrooms, locations


class RequestRental(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #navigation
        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame("UserHomepage"))
        button1.grid(row=0, column=1, padx=10, pady=10)
        button2 = ttk.Button(self, text="Rental Listings",
                             command=lambda: controller.show_frame("RentalListings"))
        button2.grid(row=0, column=2, padx=10, pady=10)
        button3 = ttk.Button(self, text="Available agents",
                             command=lambda: controller.show_frame("ListOfAvailableAgents"))
        button3.grid(row=0, column=3, padx=10, pady=10)
        button4 = ttk.Button(self, text="Switch Account",
                             command=lambda: controller.show_frame("AgentHomepage"))
        button4.grid(row=0, column=4, padx=10, pady=10)

        # Left side - Current listed properties
        label = ttk.Label(self, text="Request Rental Listing", font=LARGEFONT)
        label.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        self.selected_location = tk.StringVar(value="Kapsabet")
        self.selected_bedroom = tk.StringVar(value="1")

        # Right side - Form to upload new rental

        # Create labels and entry fields for each input
        phone_label = tk.Label(self, text="Phone:")
        self.phone_entry = tk.Entry(self)

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
        phone_label.grid(row=2, column=1, padx=5, pady=5)
        self.phone_entry.grid(row=2, column=2, padx=5, pady=5)

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
        phone = self.phone_entry.get()
        num_bedrooms = self.selected_bedroom.get()
        rental_price = self.rental_price_entry.get()
        location = self.selected_location.get()
        description = self.description_entry.get()

        # Connect to the database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='admin',
            db='pythonproject1'
        )

        try:
            # Create a cursor object to execute SQL queries
            with connection.cursor() as cursor:
                # Construct the SQL query
                sql = (
                    "INSERT INTO requests (phone, num_bedrooms, rental_price, location, description) "
                    "VALUES (%s, %s, %s, %s, %s)"
                )
                # Execute the query with the input data
                cursor.execute(sql, (phone, num_bedrooms, rental_price, location, description))
            # Commit the changes to the database
            connection.commit()
        except:
            # Roll back the changes if an error occurs
            connection.rollback()
        finally:
            # Close the database connection
            connection.close()

        # Display a success message to the user
        messagebox.showinfo("Success", "Rental listing request sent!")

        # Clear the entry fields
        self.phone_entry.delete(0, tk.END)
        self.selected_bedroom.set("1")
        self.rental_price_entry.delete(0, tk.END)
        self.selected_location.set("Kapsabet")
        self.description_entry.delete(0, tk.END)
