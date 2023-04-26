import tkinter as tk
from tkinter import ttk

from const import LARGEFONT


class RentalListings(tk.Frame):
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

        label = ttk.Label(self, text="Rental Listings", font=LARGEFONT)
        label.grid(row=1, column=4, padx=10, pady=10)

        # Create rental_card container
        rental_card = tk.Frame(self, bg="#f0f0f0", padx=10, pady=10)
        rental_card.grid(row=2, column=4, padx=10, pady=10, sticky="w")

        # Add rental details to rental_card
        rental_name = ttk.Label(rental_card, text="Moiben")
        rental_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        rental_location = ttk.Label(rental_card, text="Location: Bara C STAGE")
        rental_location.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        rental_price = ttk.Label(rental_card, text="Price: 3500")
        rental_price.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        rental_num_rooms = ttk.Label(rental_card, text="Number of Rooms: single room")
        rental_num_rooms.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        agent_contact_button = ttk.Button(rental_card, text="Contact Agent")
        agent_contact_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        # Create three more cards
        card1 = tk.Frame(self, bg="#f0f0f0", padx=10, pady=10)
        card1.grid(row=3, column=4, padx=10, pady=10, sticky="w")

        # Add rental details to rental_card
        rental_name = ttk.Label(card1, text="Pressy")
        rental_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        rental_location = ttk.Label(card1, text="Location: BARA C")
        rental_location.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        rental_price = ttk.Label(card1, text="Price: 4000/Month")
        rental_price.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        rental_num_rooms = ttk.Label(card1, text="Number of Rooms: Bedsitter")
        rental_num_rooms.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        agent_contact_button = ttk.Button(card1, text="Contact Agent")
        agent_contact_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")



