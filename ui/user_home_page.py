import tkinter as tk
from tkinter import ttk

from const import LARGEFONT


class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Welcome", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

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



