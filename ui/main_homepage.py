import tkinter as tk

class MainHomepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create a welcome message
        welcome_label = tk.Label(self, text="Welcome to My Real Estate App!", font=("Helvetica", 20))
        welcome_label.grid(row=0, columnspan=5, padx=10, pady=10)

        # Create a login button
        login_button = tk.Button(self, text="Login", font=("Helvetica", 14),
                                 command=lambda: controller.show_frame("LoginPage"))
        login_button.grid(row=1, column=1, padx=10, pady=10)

        # Create a signup button
        signup_button = tk.Button(self, text="Signup", font=("Helvetica", 14),
                                  command=lambda: controller.show_frame("SignupPage"))
        signup_button.grid(row=1, column=2, padx=10, pady=10)