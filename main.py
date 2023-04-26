import tkinter as tk

from ui.agent_home_page import AgentHomepage
from ui.pending_requests import PendingRequests
from ui.user_home_page import Homepage
from ui.add_rental_listing import AddRentalListing
from ui.list_of_available_agents import ListOfAvailableAgents
from ui.rental_details import RentalDetails
from ui.rental_listings import RentalListings
from ui.request_rental_form import RequestRental
from ui.user_profile import UserProfile


class RealEstateApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Set window size and position
        self.geometry("1080x720")

        # Create a canvas with a scrollbar
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        canvas.configure(yscrollcommand=scrollbar.set)

        # Add the scrollbar and the canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.frames = {}

        for F in (Homepage, AddRentalListing, RentalDetails, UserProfile, RentalListings, ListOfAvailableAgents, RequestRental, AgentHomepage, PendingRequests):
            frame = F(scrollable_frame, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Homepage")

    def show_frame(self, cont):
        if cont in self.frames:
            frame = self.frames[cont]
            frame.tkraise()
        else:
            print(f"Error: {cont} does not exist in frames dictionary.")


app = RealEstateApp()
app.mainloop()
