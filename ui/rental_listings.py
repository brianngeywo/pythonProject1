import tkinter as tk
from tkinter import ttk
import pymysql.cursors
from const import LARGEFONT


class RentalListings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # navigation
        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame("AgentHomepage"))
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
        button5 = ttk.Button(self, text="Switch to User",
                             command=lambda: controller.show_frame("UserHomepage"))
        button5.grid(row=0, column=5, padx=10, pady=10)

        label = ttk.Label(self, text="Rental Listings", font=LARGEFONT)
        label.grid(row=1, column=4, padx=10, pady=10)

        # Create rental_cards container
        self.rental_cards = tk.Frame(self, bg="#f0f0f0", padx=10, pady=10)
        self.rental_cards.grid(row=2, column=4, padx=10, pady=10, sticky="w")

        # Add a "Refresh" button
        refresh_button = ttk.Button(self, text="Refresh Listings", command=self.refresh_rentals)
        refresh_button.grid(row=3, column=4, padx=10, pady=10, sticky="w")

        # Fetch rental data from database
        self.fetch_rentals()

    def fetch_rentals(self):
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='admin',
                                     db='pythonproject1',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            cursor = connection.cursor()
            # Fetch rental data from database
            sql = "SELECT * FROM rental"
            cursor.execute(sql)
            rentals = cursor.fetchall()

            # Display rental data on the page
            for index, rental in enumerate(rentals):
                rental_card = tk.Frame(self.rental_cards, bg="#f0f0f0", padx=10, pady=10)
                rental_card.grid(row=index, column=0, padx=10, pady=10, sticky="w")

                rental_location = ttk.Label(rental_card, text="Location: %s" % rental['location'])
                rental_location.grid(row=1, column=0, padx=5, pady=5, sticky="w")

                rental_price = ttk.Label(rental_card, text="Price: %s" % rental['rental_price'])
                rental_price.grid(row=2, column=0, padx=5, pady=5, sticky="w")
                rental_bedrooms = ttk.Label(rental_card, text="Bedrooms: %s" % rental['num_bedrooms'])
                rental_bedrooms.grid(row=3, column=0, padx=5, pady=5, sticky="w")

                rental_description = ttk.Label(rental_card, text="Description: %s" % rental['description'])
                rental_description.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        finally:
            # Close the database connection
            connection.close()

    def refresh_rentals(self):
        # Clear the existing rental cards
        for widget in self.rental_cards.winfo_children():
            widget.destroy()

        # Fetch rental data from database
        self.fetch_rentals()
