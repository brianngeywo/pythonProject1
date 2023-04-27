import tkinter as tk
from tkinter import ttk

from const import LARGEFONT


class ListOfAvailableAgents(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # navigation
        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame("UserHomepage"))
        button1.grid(row=0, column=1, padx=10, pady=10)
        button2 = ttk.Button(self, text="Rental Listings",
                             command=lambda: controller.show_frame("RentalListings"))
        button2.grid(row=0, column=2, padx=10, pady=10)
        button3 = ttk.Button(self, text="Request new listing",
                             command=lambda: controller.show_frame("RequestRental"))
        button3.grid(row=0, column=3, padx=10, pady=10)
        button4 = ttk.Button(self, text="Switch Account",
                             command=lambda: controller.show_frame("UserHomepage"))
        button4.grid(row=0, column=4, padx=10, pady=10)

        main_label = ttk.Label(self, text="List of available agents", font=LARGEFONT)
        main_label.grid(row=1, column=4, padx=10, pady=10)

        # Create agent_card container
        agent_card = tk.Frame(self, bg="#f0f0f0", padx=10, pady=10)
        agent_card.grid(row=2, column=4, padx=10, pady=10, sticky="w")

        # Add agent details to agent_card
        agent_name = ttk.Label(agent_card, text="Agent Name")
        agent_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        agent_location = ttk.Label(agent_card, text="Location")
        agent_location.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        agent_num_rentals = ttk.Label(agent_card, text="Number of rentals uploaded")
        agent_num_rentals.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        agent_contact_button = ttk.Button(agent_card, text="Contact Agent")
        agent_contact_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        # Create agent_card2 container
        agent_card = tk.Frame(self, bg="#f0f0f0", padx=10, pady=10)
        agent_card.grid(row=3, column=4, padx=10, pady=10, sticky="w")

        # Add agent details to agent_card
        agent_name = ttk.Label(agent_card, text="Agent Name")
        agent_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        agent_location = ttk.Label(agent_card, text="Location")
        agent_location.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        agent_num_rentals = ttk.Label(agent_card, text="Number of rentals uploaded")
        agent_num_rentals.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        agent_contact_button = ttk.Button(agent_card, text="Contact Agent")
        agent_contact_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        # Create two more container cards below agent_card
        # Create agent_card3 container
        agent_card = tk.Frame(self, bg="#f0f0f0", padx=10, pady=10)
        agent_card.grid(row=4, column=4, padx=10, pady=10, sticky="w")

        # Add agent details to agent_card
        agent_name = ttk.Label(agent_card, text="Agent Name")
        agent_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        agent_location = ttk.Label(agent_card, text="Location")
        agent_location.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        agent_num_rentals = ttk.Label(agent_card, text="Number of rentals uploaded")
        agent_num_rentals.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        agent_contact_button = ttk.Button(agent_card, text="Contact Agent")
        agent_contact_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

