import tkinter as tk
from tkinter import ttk

from const import LARGEFONT


class AgentHomepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Homepage", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Add new rental",
                             command=lambda: controller.show_frame("AddRentalListing"))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Pending Requests",
                             command=lambda: controller.show_frame("PendingRequests"))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Your Rental Listings",
                             command=lambda: controller.show_frame("RentalListings"))
        button3.grid(row=3, column=1, padx=10, pady=10)

        button4 = ttk.Button(self, text="Your Account",
                             command=lambda: controller.show_frame("UserProfile"))
        button4.grid(row=4, column=1, padx=10, pady=10)

        button5 = ttk.Button(self, text="Switch to user view",
                             command=lambda: controller.show_frame("Homepage"))
        button5.grid(row=5, column=1, padx=10, pady=10)

