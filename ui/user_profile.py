import tkinter as tk
from tkinter import ttk

from const import LARGEFONT


class UserProfile(tk.Frame):
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

        # create the label for user profile
        label = ttk.Label(self, text="User Profile", font=LARGEFONT)
        label.grid(row=1, column=4, padx=10, pady=10)

        # Create agent_card container
        agent_card = tk.Frame(self, bg="#f0f0f0", padx=10, pady=10)
        agent_card.grid(row=2, column=4, padx=10, pady=10, sticky="w")

        # Add agent details to agent_card
        agent_name_label = ttk.Label(agent_card, text="Name: Brian Ngeywo")
        agent_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        agent_contact_label = ttk.Label(agent_card, text="Contact Information: agent1@nyumbafast.com")
        agent_contact_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        agent_location_label = ttk.Label(agent_card, text="Location: Eldoret")
        agent_location_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        agent_num_rentals_label = ttk.Label(agent_card, text="Number of Rentals Uploaded: 24")
        agent_num_rentals_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        agent_ratings_label = ttk.Label(agent_card, text="Ratings/Reviews from Previous Clients: 4.7")
        agent_ratings_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        agent_specialization_label = ttk.Label(agent_card, text="Specialization: Family residents")
        agent_specialization_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        agent_experience_label = ttk.Label(agent_card, text="Years of Experience: 5yrs")
        agent_experience_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        agent_certifications_label = ttk.Label(agent_card, text="Certifications/Licenses: None")
        agent_certifications_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

        # agent_clients_label = ttk.Label(agent_card, text="Current/Past Clients")
        # agent_clients_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        #
        # agent_bio_label = ttk.Label(agent_card, text="Personal Bio/Summary of Services and Experience: ")
        # agent_bio_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")

        agent_contact_button = ttk.Button(agent_card, text="Contact Agent")
        agent_contact_button.grid(row=8, column=0, padx=5, pady=5, sticky="w")






