import tkinter as tk
from tkinter import ttk

from const import LARGEFONT, MEDIUMFONT


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

        # Section explaining the platform
        platform_label = ttk.Label(self, text="About the Platform", font=MEDIUMFONT)
        platform_label.grid(row=1, column=4, padx=10, pady=10)

        platform_text = "Looking for a hassle-free way to earn extra income?\n" \
                        "Become a local agent on our platform and help foreigners find their dream home. \n" \
                        "Here's why you'll love it:\n"\
                        "   - Earn money by finding the perfect home for someone who needs it\n"\
                        "   - Work at your own pace and schedule\n"\
                        "   - Get paid quickly and easily through the platform\n"\
                        "   - Gain valuable experience in real estate and build your professional network\n"\
                        "Join our platform today and start making money doing what you love."

        platform_description = ttk.Label(self, text=platform_text, font=("Arial", 12), wraplength=650)
        platform_description.grid(row=2, column=4, padx=10, pady=10)

        # Steps of how the platform works
        step1_label = ttk.Label(self, text="Step 1: Register as an agent", font=MEDIUMFONT)
        step1_label.grid(row=3, column=4, padx=10, pady=10)

        step1_text = "The agent signs up on the platform and " \
                     "creates a profile with their information and expertise in finding rental properties."

        step1_description = ttk.Label(self, text=step1_text, font=("Arial", 12), wraplength=650)
        step1_description.grid(row=4, column=4, padx=10, pady=10)

        step2_label = ttk.Label(self, text="Step 2: View requests", font=MEDIUMFONT)
        step2_label.grid(row=5, column=4, padx=10, pady=10)

        step2_text ="The agent can view requests made by " \
                    "foreign users who are looking for rental properties in the agent's local area."

        step2_description = ttk.Label(self, text=step2_text, font=("Arial", 12), wraplength=650)
        step2_description.grid(row=6, column=4, padx=10, pady=10)

        step3_label = ttk.Label(self, text="Step 3: Find a suitable house", font=MEDIUMFONT)
        step3_label.grid(row=7, column=4, padx=10, pady=10)

        step3_text ="Using their expertise and knowledge of the local area, " \
                    "the agent finds a suitable rental property for the foreign user."

        step3_description = ttk.Label(self, text=step3_text, font=("Arial", 12), wraplength=650)
        step3_description.grid(row=8, column=4, padx=10, pady=10)

        step4_label = ttk.Label(self, text="Step 4: Upload the property", font=MEDIUMFONT)
        step4_label.grid(row=9, column=4, padx=10, pady=10)

        step4_text ="The agent uploads details of the property to the platform, including pictures, " \
                    "location, rental price, and other relevant information."

        step4_description = ttk.Label(self, text=step4_text, font=("Arial", 12), wraplength=650)
        step4_description.grid(row=10, column=4, padx=10, pady=10)

        step5_label = ttk.Label(self, text="Step 5: Notify the foreign user", font=MEDIUMFONT)
        step5_label.grid(row=11, column=4, padx=10, pady=10)

        step5_text ="The platform sends a notification to the " \
                    "foreign user with the details of the property found by the agent."

        step5_description = ttk.Label(self, text=step5_text, font=("Arial", 12), wraplength=650)
        step5_description.grid(row=12, column=4, padx=10, pady=10)

        step6_label = ttk.Label(self, text="Step 6: Foreign user accepts or declines", font=MEDIUMFONT)
        step6_label.grid(row=13, column=4, padx=10, pady=10)

        step6_text ="The foreign user can review the property details " \
                    "and either accept or decline the rental property found by the agent."

        step6_description = ttk.Label(self, text=step6_text, font=("Arial", 12), wraplength=650)
        step6_description.grid(row=14, column=4, padx=10, pady=10)

        step7_label = ttk.Label(self, text="Step 7: Payment", font=MEDIUMFONT)
        step7_label.grid(row=15, column=4, padx=10, pady=10)

        step7_text ="If the foreign user accepts the rental property, " \
                    "payment is processed through the platform."

        step7_description = ttk.Label(self, text=step7_text, font=("Arial", 12), wraplength=650)
        step7_description.grid(row=16, column=4, padx=10, pady=10)

        step8_label = ttk.Label(self, text="Step 8: Leave a review", font=MEDIUMFONT)
        step8_label.grid(row=17, column=4, padx=10, pady=10)

        step8_text ="The foreign user can leave a review for the agent regarding their experience with the rental property found. " \
                    "The review will be available on the agent's profile for other users to see."

        step8_description = ttk.Label(self, text=step8_text, font=("Arial", 12), wraplength=650)
        step8_description.grid(row=18, column=4, padx=10, pady=10)

