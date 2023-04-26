import tkinter as tk
from tkinter import ttk

from const import LARGEFONT, MEDIUMFONT


class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #navigation
        button1 = ttk.Button(self, text="Rental Listings",
                             command=lambda: controller.show_frame("RentalListings"))
        button1.grid(row=3, column=1, padx=15, pady=15)

        button2 = ttk.Button(self, text="List of available agents",
                             command=lambda: controller.show_frame("ListOfAvailableAgents"))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Request new rental",
                             command=lambda: controller.show_frame("RequestRental"))
        button3.grid(row=1, column=1, padx=10, pady=10)

        button4 = ttk.Button(self, text="Your Account",
                             command=lambda: controller.show_frame("UserProfile"))
        button4.grid(row=4, column=1, padx=10, pady=10)

        button5 = ttk.Button(self, text="Switch to agent view",
                             command=lambda: controller.show_frame("AgentHomepage"))
        button5.grid(row=5, column=1, padx=10, pady=10)

        #main page
        label = ttk.Label(self, text="Welcome", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # Section explaining the platform
        platform_label = ttk.Label(self, text="About the Platform", font=MEDIUMFONT)
        platform_label.grid(row=1, column=4, padx=10, pady=10)

        platform_text = "Our platform is designed to help connect people" \
                        " who are looking for a house with locals who have the expertise" \
                        " and knowledge to help them find the perfect home. " \
                        "If you're moving to a new town or " \
                        "just don't have the time to search for a new place, " \
                        "our platform can help you find the right home quickly and easily. " \
                        "Here's how it works:"

        platform_description = ttk.Label(self, text=platform_text, font=("Arial", 12),wraplength=650)
        platform_description.grid(row=2, column=4, padx=10, pady=10)

        # Steps of how the platform works
        step1_label = ttk.Label(self, text="How it Works - User Posts a Request", font=MEDIUMFONT)
        step1_label.grid(row=3, column=4, padx=10, pady=10)

        step1_text = "When a user posts a request for a house, a local expert will be notified " \
                     "and will begin searching for the perfect place to meet their needs. " \
                     "The local expert may not own any houses themselves, " \
                     "but they have extensive knowledge of the local housing market and " \
                     "can quickly find suitable options."

        step1_description = ttk.Label(self, text=step1_text, font=("Arial", 12),wraplength=650)
        step1_description.grid(row=4, column=4, padx=10, pady=10)

        step2_label = ttk.Label(self, text="How it Works - Local Expert Uploads House Options", font=MEDIUMFONT)
        step2_label.grid(row=5, column=4, padx=10, pady=10)

        step2_text = "Once the local expert has found some suitable options, " \
                     "they will upload them to the platform for the user to review. " \
                     "The user can then decide which one they like best and either accept it or " \
                     "ask the local expert to continue searching."

        step2_description = ttk.Label(self, text=step2_text, font=("Arial", 12),wraplength=650)
        step2_description.grid(row=6, column=4, padx=10, pady=10 )

        step3_label = ttk.Label(self, text="How it Works - Payment and Review", font=MEDIUMFONT)
        step3_label.grid(row=7, column=4, padx=10, pady=10)

        step3_text = " If the user decides to accept a house, they will pay for it through our secure platform. " \
                     "Once the payment has been processed, the user can move in and start enjoying their new home. " \
                     "The user can also leave a review of the local expert to help future users make informed decisions."

        step3_description = ttk.Label(self, text=step3_text, font=("Arial", 12), wraplength=650)
        step3_description.grid(row=8, column=4, padx=10, pady=10)






