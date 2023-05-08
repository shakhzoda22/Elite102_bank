#I used numerous sources provided by Code2College to aid me in doing this Banking project: 
#Using Tkinter https://www.youtube.com/watch?v=RFwTk4twaOI
#Helping me with the Tkinter App setup https://www.youtube.com/watch?v=itRLRfuL_PQ
#Johan Godinho's banking system video part 1 https://www.youtube.com/watch?v=itRLRfuL_PQ

import tkinter as tk
import mysql.connector

 # Connect to the MySQL database
conn = mysql.connector.connect(
    user="root",
    database="elite_bank",
    password="Nafisa@2008"
)
cursor = conn.cursor()


def search_user():
    # Get the entered user ID
    entered_username = user_id_entry.get()

    # Check if the user exists in the database
    # query = f"SELECT * FROM users WHERE username = '{entered_username}'"
    query = f"select * from users"
    cursor.execute(query)
    user = cursor.fetchone() 
    breakpoint()


    if user:
        # Save the user ID and balance for future reference
        global username, balance
        username = user[0]
        balance = user[3]

        # Update the balance label
        balance_label.config(text=f"Balance: ${balance}")

        # Enable the transaction buttons
        withdraw_button.config(state=tk.NORMAL)
        deposit_button.config(state=tk.NORMAL)
    else:
        # Show an error message
        error_label.config(text="User not found")

def withdraw():
    # Get the entered withdrawal amount
    withdrawal_amount = float(withdraw_entry.get())

    if balance >= withdrawal_amount:
        # Update the balance
        balance -= withdrawal_amount
        query = f"UPDATE users SET balance = {balance} WHERE id = {user_id}"
        cursor.execute(query)
        conn.commit()

        # Update the balance label
        balance_label.config(text=f"Balance: ${balance}")
    else:
        error_label.config(text="Insufficient funds")

def deposit():
    # Get the entered deposit amount
    deposit_amount = float(deposit_entry.get())

    # Update the balance
    balance += deposit_amount
    query = f"UPDATE users SET balance = {balance} WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

    # Update the balance label
    balance_label.config(text=f"Balance: ${balance}")

# Create the main window 
root = tk.Tk()
root.title("Banking System")

frame = tk.Frame(root, bg='#3e646c')
frame.place(relwidth=0.8, relheight=0.9, rely=0.1, relx=0.1 )

# Create and place the user ID form widgets
user_id_label = tk.Label(root, text="User ID:")
user_id_label.pack()
user_id_entry = tk.Entry(root)
user_id_entry.pack()

search_button = tk.Button(root, text="Search", command=search_user)
search_button.pack()

# Create and place the withdrawal form widgets
withdraw_label = tk.Label(root, text="Withdraw Amount:")
withdraw_label.pack()
withdraw_entry = tk.Entry(root)
withdraw_entry.pack()

withdraw_button = tk.Button(root, text="Withdraw", command=withdraw, state=tk.DISABLED)
withdraw_button.pack()

# Create and place the deposit form widgets
deposit_label = tk.Label(root, text="Deposit Amount:")
deposit_label.pack()
deposit_entry = tk.Entry(root)
deposit_entry.pack()

deposit_button = tk.Button(root, text="Deposit", command=deposit, state=tk.DISABLED)
deposit_button.pack()

# Create and place the balance label
balance_label = tk.Label(root, text='balance: ')
balance_label.pack()

# Create and place the error message label
error_label = tk.Label(root, text='')
error_label.pack()

root.mainloop()

conn.close()


# import tkinter as tk
# import mysql.connector

#  # Connect to the MySQL database
# conn = mysql.connector.connect(
#     user="root",
#     database="elite_bank",
#     password="Nafisa@2008"
# )
# cursor = conn.cursor()

# def login():
#     # Get the entered username and password
#     entered_username = username_entry.get()
#     entered_password = password_entry.get()

#     # Check if the user exists in the database
#     query = f"SELECT * FROM users WHERE username = '{entered_username}' AND password = '{entered_password}'"
#     cursor.execute(query)
#     user = cursor.fetchone()

#     if user:
#         # Save the user ID and balance for future reference
#         global user_id, balance
#         user_id = user[0]
#         balance = user[3]

#         # Update the balance label
#         balance_label.config(text=f"Balance: ${balance}")

#         # Enable the transaction buttons
#         transfer_button.config(state=tk.NORMAL)
#         check_balance_button.config(state=tk.NORMAL)
#     else:
#         # Show an error message
#         error_label.config(text="Invalid username or password")

# def transfer():
#     # Get the entered recipient username and transfer amount
#     recipient_username = recipient_entry.get()
#     transfer_amount = int(amount_entry.get())

#     # Check if the recipient exists in the database
#     query = f"SELECT * FROM users WHERE username = '{recipient_username}'"
#     cursor.execute(query)
#     recipient = cursor.fetchone()

#     if recipient:
#         recipient_id = recipient[0]
#         recipient_balance = recipient[3]

#         if balance >= transfer_amount:
#             # Update the sender's balance
#             balance -= transfer_amount
#             query = f"UPDATE users SET balance = {balance} WHERE id = {user_id}"
#             cursor.execute(query)

#             # Update the recipient's balance
#             recipient_balance += transfer_amount
#             query = f"UPDATE users SET balance = {recipient_balance} WHERE id = {recipient_id}"
#             cursor.execute(query)

#             # Commit the changes to the database
#             conn.commit()

#             # Update the balance label
#             balance_label.config(text=f"Balance: ${balance}")
#         else:
#             error_label.config(text="Insufficient funds")
#     else:
#         error_label.config(text="Recipient not found")

# def check_balance():
#     balance_label.config(text=f"Balance: ${balance}")

# # Create the main root
# root = tk.Tk()
# root.title("WELCOME TO THE BANK")

# frame = tk.Frame(root, bg='#3e646c')
# frame.place(relwidth=0.8, relheight=0.9, rely=0.1, relx=0.1 )


# # Create and place the login form widgets
# username_label = tk.Label(root, text="Username:")
# username_label.pack()
# username_entry = tk.Entry(root)
# username_entry.pack()

# password_label = tk.Label(root, text="Password:")
# password_label.pack()
# password_entry = tk.Entry(root, show="*")
# password_entry.pack()

# login_button = tk.Button(root, text="Login", command=login)
# login_button.pack()

# # Create and place the transaction form widgets
# recipient_label = tk.Label(root, text="Recipient:")
# recipient_label.pack()
# recipient_entry = tk.Entry(root)
# recipient_entry.pack()

# amount_label = tk.Label(root, text="Amount:")
# amount_label.pack()
# amount_entry = tk.Entry(root)
# amount_entry.pack()

# transfer_button = tk.Button(root, text="Transfer", command=transfer, state=tk.DISABLED)
# transfer_button.pack()

# check_balance_button = tk.Button(root, text="Check Balance", command=check_balance, state=tk.DISABLED)
# check_balance_button.pack()

#  # Create and place the balance label
# balance_label = tk.Label(root, text='balance: ')
# balance_label.pack()

# root.mainloop()

# conn.close()

# import mysql.connector

# connection = mysql.connector.connect(user = "root", database = "elite_bank", password="Nafisa@2008")

# import tkinter as tk
# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect('elite_bank.db')
# cursor = conn.cursor()

# def login():
#     # Get the entered username and password
#     entered_username = username_entry.get()
#     entered_password = password_entry.get()

#     # Check if the user exists in the database
#     query = f"SELECT * FROM users WHERE username = '{entered_username}' AND password = '{entered_password}'"
#     cursor.execute(query)
#     user = cursor.fetchone()

#     if user:
#         # Save the user ID and balance for future reference
#         global user_id, balance
#         user_id = user[0]
#         balance = user[3]

#         # Update the balance label
#         balance_label.config(text=f"Balance: ${balance}")

#         # Enable the transaction buttons
#         transfer_button.config(state=tk.NORMAL)
#         check_balance_button.config(state=tk.NORMAL)
#     else:
#         # Show an error message
#         error_label.config(text="Invalid username or password")

# def transfer():
#     # Get the entered recipient username and transfer amount
#     recipient_username = recipient_entry.get()
#     transfer_amount = int(amount_entry.get())

#     # Check if the recipient exists in the database
#     query = f"SELECT * FROM users WHERE username = '{recipient_username}'"
#     cursor.execute(query)
#     recipient = cursor.fetchone()

#     if recipient:
#         recipient_id = recipient[0]
#         recipient_balance = recipient[3]

#         if balance >= transfer_amount:
#             # Update the sender's balance
#             balance -= transfer_amount
#             query = f"UPDATE users SET balance = {balance} WHERE id = {user_id}"
#             cursor.execute(query)

#             # Update the recipient's balance
#             recipient_balance += transfer_amount
#             query = f"UPDATE users SET balance = {recipient_balance} WHERE id = {recipient_id}"
#             cursor.execute(query)

#             # Commit the changes to the database
#             conn.commit()

#             # Update the balance label
#             balance_label.config(text=f"Balance: ${balance}")
#         else:
#             error_label.config(text="Insufficient funds")
#     else:
#         error_label.config(text="Recipient not found")

# def check_balance():
#     balance_label.config(text=f"Balance: ${balance}")

# # Create the main root
# root = tk.Tk()
# root.title("WELCOME TO THE BANK")

# # Create and place the login form widgets
# username_label = tk.Label(root, text="Username:")
# username_label.pack()
# username_entry = tk.Entry(root)
# username_entry.pack()

# password_label = tk.Label(root, text="Password:")
# password_label.pack()
# password_entry = tk.Entry(root, show="*")
# password_entry.pack()

# login_button = tk.Button(root, text="Login", command=login)
# login_button.pack()

# # Create and place the transaction form widgets
# recipient_label = tk.Label(root, text="Recipient:")
# recipient_label.pack()
# recipient_entry = tk.Entry(root)
# recipient_entry.pack()

# amount_label = tk.Label(root, text="Amount:")
# amount_label.pack()
# amount_entry = tk.Entry(root)
# amount_entry.pack()

# transfer_button = tk.Button(root, text="Transfer", command=transfer, state=tk.DISABLED)
# transfer_button.pack()

# check_balance_button = tk.Button(root, text="Check Balance", command=check_balance, state=tk.DISABLED)
# check_balance_button.pack()

# # Create and place the balance label
# balance_label = tk.Label(root, text='balance: ')
# balance_label.pack()

# root.mainloop()

# conn.close()
