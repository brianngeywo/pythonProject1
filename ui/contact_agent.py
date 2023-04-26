import tkinter as tk
from tkinter import ttk

from const import LARGEFONT


class ContactAgent(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # navigation
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

        label = ttk.Label(self, text="Contact Agent", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)




