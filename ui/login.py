import tkinter as tk
import pymysql.cursors




class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create a title label
        title_label = tk.Label(self, text="Login", font=("Helvetica", 20))
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create a username label and entry field
        username_label = tk.Label(self, text="Username:")
        username_label.grid(row=1, column=0, padx=10, pady=10)
        username_entry = tk.Entry(self)
        username_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create a password label and entry field
        password_label = tk.Label(self, text="Password:")
        password_label.grid(row=2, column=0, padx=10, pady=10)
        password_entry = tk.Entry(self, show="*")
        password_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create a login button
        login_button = tk.Button(self, text="Login", command=lambda: submit_form(username_entry.get(), password_entry.get()))
        login_button.grid(row=3, column=1, padx=10, pady=10)

        # Create a back button
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainHomepage"))
        back_button.grid(row=3, column=0, padx=10, pady=10)

        def submit_form(username, password):
            # Connect to the database
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="admin",
                database="pythonproject1",
                cursorclass=pymysql.cursors.DictCursor
            )

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Execute the SQL query to fetch the user with the given username and password
            sql = "SELECT * FROM users WHERE username=%s AND password=%s"
            values = (username, password)
            cursor.execute(sql, values)

            # Fetch the result of the query
            result = cursor.fetchone()

            # Close the database connection
            connection.close()

            if result:
                # Display a success message
                print("User", username, "logged in successfully")
                controller.show_frame("AddRentalListing")
            else:
                # Display an error message
                print("Invalid username or password")