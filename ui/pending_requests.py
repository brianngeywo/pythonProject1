import tkinter as tk
from tkinter import ttk
import pymysql.cursors
from const import LARGEFONT


class PendingRequests(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # navigation
        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame("AgentHomepage"))
        button1.grid(row=0, column=1, padx=10, pady=10)
        button2 = ttk.Button(self, text="Rental Listings",
                             command=lambda: controller.show_frame("RentalListings"))
        button2.grid(row=0, column=2, padx=10, pady=10)

        # refresh button
        button_refresh = ttk.Button(self, text="Refresh", command=self.refresh_requests)
        button_refresh.grid(row=4, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Pending Requests", font=LARGEFONT)
        label.grid(row=2, column=1, padx=10, pady=10)

        # treeview to display requests
        self.treeview = ttk.Treeview(self, columns=("Phone", "Bedrooms", "Price", "Location", "Description"), show="headings")
        self.treeview.grid(row=3, column=1, columnspan=5, padx=10, pady=10)
        self.treeview.heading("Phone", text="Phone")
        self.treeview.heading("Bedrooms", text="Bedrooms")
        self.treeview.heading("Price", text="Price")
        self.treeview.heading("Location", text="Location")
        self.treeview.heading("Description", text="Description")

        # populate treeview with requests
        self.refresh_requests()

    def refresh_requests(self):
        # clear existing items in treeview
        self.treeview.delete(*self.treeview.get_children())

        # connect to database and fetch requests
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='admin',
                                     db='pythonproject1',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM requests"
                cursor.execute(sql)
                requests = cursor.fetchall()
                for request in requests:
                    self.treeview.insert("", "end", values=(request["phone"], request["num_bedrooms"], request["rental_price"], request["location"], request["description"]))

        finally:
            connection.close()
