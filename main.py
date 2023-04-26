import mysql.connector

# Define database credentials
credentials = {
    "user": "root",
    "database": "Elite_102",
    "password": "Nafisa@2008"
}

# Create a database connection object
connection = mysql.connector.connect(**credentials)
connection.autocommit = False

# Execute a raw query
def execute(querytext, params=tuple()):
    try:
        cursor = connection.cursor()
        cursor.execute(querytext, params)
        data = [x for x in cursor]
        cursor.close()
        return (True, data)
    except Exception as err:
        cursor.close()
        return (False, err)

# Execute a select query
def query(querytest, params=tuple()):
    result = execute(querytest, params)
    # If query fails, return err as is
    # Otherwise, return structured data
    if not result[0]:
        return result
    else:
        return (True, [structure(x) for x in result[1]])

# Turn tuples returned by MySQL into a dictionary
def structure(raw):
    keys = ["id", "username", "password", "balance", "admin"]
    # Assign each tuple value to a key
    dictionary = dict(zip(keys, list(raw)))
    # Replace 1/0 booleans with Python booleans
    dictionary["admin"] = bool(dictionary["admin"])
    return dictionary

# Register a new user
def register(username, password):
    result = execute('INSERT INTO users (username, password, balance, admin) VALUES (%s, %s, 0, false);', (username, password))
    connection.commit()
    return result[0]

# Login to an account
def login(username, password):
    user = query("SELECT * FROM users WHERE username=%s", (username,))
    # Error or nonexistent user
    if not user[0] or not user[1]:
        return False
    else:
        return password == user[1][0]["password"]

# Get user ID from username
def getid(username):
    user = query("SELECT * FROM users WHERE username=%s", (username,))
    # Error or no user found
    if not user[0] or not user[1]:
        return -1
    else:
        return user[1][0]["id"]

# Delete account
def delete_account(username, password):
    # Make sure user is authenticated to delete account
    if not login(username, password):
        return False
    q = execute("DELETE FROM users WHERE username=%s", (username,))
    connection.commit()
    return q[0]

# Change username
def username_change(uid, newname, password):
    q = execute("UPDATE users SET username=%s WHERE id=%s AND password=%s", (newname, uid, password))
    connection.commit()
    return q[0]

# Change password
def change_password(uid, oldpass, newpass):
    q = query("SELECT * FROM users WHERE id=%s AND password=%s", (uid, oldpass))
    if not q[0] or not q[1]:
        return False
    q = execute("UPDATE users SET password=%s WHERE id=%s AND password=%s", (newpass, uid, oldpass))
    connection.commit()
    return q[0]

# Check balance
def balance(uid):
    b = query("SELECT * FROM users WHERE id=%s", (uid,))
    if not b[0] or not b[1]:
        return float(0)
    else:
        return b[1][0]["balance"]

#Withdraw money
def withdraw (uid, amount): 
    deposit(uid, 0 - amount)


#Wire money between accounts
def wire(sender, recipient, amount) :
    s = withdraw(sender, amount)
    r = deposit(recipient, amount)

    return s and r

# Deposit money
def deposit(uid, amount):
    bal = balance


def main():
    while True:
        action = input("What do you want to do?").lower().strip()
        if action == "login":
            username = input("Username: ")
            password = input("Password: ")
            success = login(username, password)
            if success:
                print("Success")
            else:
                print("Login Failed")



# import mysql.connector


# credentials = {
#     "user": "root",
#     "database": "Elite_102",
#     "password": "Nafisa@2008"
# }

# connection = mysql.connector.connect(**credentials)
# connection.autocommit = False



# #Execute a raw query
# def execute(querytext, params = tuple()):
#     try:
#         cursor = connection.cursor()

#         cursor.execute(querytext, params)

#         data = [x for x in cursor]

#         cursor.close()
#         return (True, data)
#     except Exception as err:
#         cursor.close()
#         return (False, err)
    
# #Execute a select query
# def query(querytest, params = tuple()):
#     result = execute(querytest, params)

#     #If query fails, return err as is
#     #Otherwise, return structured data
#     if not result[0]:
#         return result
#     else:
#         return (True, [structure(x) for x in result[1]])
    

# #Turn tuples returned by MySQL into a dictionary
# def structure(raw):
#     keys = ["id", "username", "password", "balance", "admin"]

#     #Assign each tupe value to a key
#     dictionary = dict(
#         zip(keys, list(raw))
#     )

#     #Replease 1/0 booleans with Python booleans
#     if dictionary["admin"] == 1:
#         dictionary["admin"] = True
#     else:
#         dictionary["admin"] = False

#     return dictionary

# def register(username, password):
#     result = execute(f'insert into users (username, password, balance, admin) values (%s, %s, 0, false);', (username, password))
#     print(result)

#     connection.commit()
#     return result[0]

# #Login to an account
# def login(username, password):
#     #Find the user trying to log in
#     user = query("select * from users where username=%s", (username,))
#     print(user)

#     #Error or nonexistent user
#     if not user[0] or len(user[1]) < 1:
#         return False
#     else:
#         return password == user[1][0]["password"]

# #Get user ID from username
# def getid(username):
#     user = query("select * from users where username=%s", (username,))
    
#     #Error or no user found
#     if not user[0] or len(user[1]) < 1:
#         return -1
#     else:
#         return user[1][0]["id"]

# #Delete account
# def delete_account(username, password):
#     #make sure user is authenticated to delete account
#     if not login(username, password):
#         return False
    
#     q = execute("delete from users where username=%s", (username,))
#     connection.commit()

#     return q[0]

# #Change username
# def username_change (uid, newname, password) :
#     q = execute("update users set username=%s where id=%s", (newname, uid))
#     connection.commit()

#     return q[0]

# def change_password(uid, oldpass, newpass) :
#     q = query("select * from users where id=%s and password=%s", (uid, oldpass))
#     if not q[0]:
#         return False
#     q = execute("update users set password=%s where id=%s and password=%s", (newpass, uid, oldpass))
#     connection.commit()

# #Check balance
# def balance(uid):
#     b = query("select * from users where id=%s", (uid, ))
#     if not b[0]:
#         return float(0)
#     else:
#         return b[1][0]["balance"]
