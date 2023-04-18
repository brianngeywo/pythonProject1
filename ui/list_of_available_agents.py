import tkinter as tk
from tkinter import ttk

from const import LARGEFONT


class ListOfAvailableAgents(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="List of available agents", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Homepage",
                             command=lambda: controller.show_frame("Homepage"))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Rental listings",
                             command=lambda: controller.show_frame("RentalListings"))
        button2.grid(row=2, column=1, padx=10, pady=10)
