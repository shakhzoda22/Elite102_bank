#I used numerous sources provided by Code2College to aid me in doing this Banking project: 
#Using Tkinter https://www.youtube.com/watch?v=RFwTk4twaOI
#Helping me with the Tkinter App setup https://www.youtube.com/watch?v=itRLRfuL_PQ
#Johan Godinho's banking system video part 1 https://www.youtube.com/watch?v=itRLRfuL_PQ

import tkinter as tk
import mysql.connector

 # Connect to the MySQL database
conn = mysql.connector.connect(
    user="root",
    database="elite_102",
    password="Nafisa@2008"
)
cursor = conn.cursor()
balance = 0 

def search_user():
    global balance
    # Get the entered user ID
    entered_username = user_id_entry.get()

    # Check if the user exists in the database
    # query = f"SELECT * FROM users WHERE username = '{entered_username}'"
    query = f"select * from users"
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone() 
    cursor.close()
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
    global balance
    # Get the entered withdrawal amount
    withdrawal_amount = float(withdraw_entry.get())

    if balance >= withdrawal_amount:
        # Update the balance
        balance -= withdrawal_amount
        query = f"UPDATE users SET balance = {balance} WHERE id = {username}"
        cursor.execute(query)
        conn.commit()

        # Update the balance label
        balance_label.config(text=f"Balance: ${balance}")
    else:
        error_label.config(text="Insufficient funds")

def deposit():
    global balance
    # Get the entered deposit amount
    deposit_amount = float(deposit_entry.get())

    # Update the balance
    balance += deposit_amount
    query = f"UPDATE users SET balance = {balance} WHERE id = {username}"
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