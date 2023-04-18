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


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Homepage, AddRentalListing, RentalDetails, UserProfile, RentalListings, ListOfAvailableAgents, RequestRental, AgentHomepage, PendingRequests):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        print(self.frames)
        self.show_frame("Homepage")

    def show_frame(self, cont):
        if cont in self.frames:
            frame = self.frames[cont]
            frame.tkraise()
        else:
            print(f"Error: {cont} does not exist in frames dictionary.")


app = tkinterApp()
app.mainloop()
