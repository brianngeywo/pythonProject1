
import tkinter as tk

import pymysql.cursors



class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create a title label
        title_label = tk.Label(self, text="Signup", font=("Helvetica", 20))
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

        # Create a button to submit the form
        submit_button = tk.Button(self, text="Submit",
                                  command=lambda: submit_form(username_entry.get(), password_entry.get()))
        submit_button.grid(row=3, column=1, padx=10, pady=10)

        # Create a button to go back to the main page
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainHomepage"))
        back_button.grid(row=3, column=0, padx=10, pady=10)
        def submit_form(username, password):
            # Connect to the database
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='admin',
                database='pythonproject1',
                cursorclass=pymysql.cursors.DictCursor
            )

            # Create a cursor object to execute SQL queries
            with connection.cursor() as cursor:
                # Insert the new user into the database
                sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
                values = (username, password)
                cursor.execute(sql, values)

            # Commit the transaction and close the database connection
            connection.commit()
            connection.close()

            # Display a success message
            print("User", username, "created successfully")
            controller.show_frame("LoginPage")
