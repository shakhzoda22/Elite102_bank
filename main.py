# main file 
import db
import functions as f
from flask import Flask
mysql-connector-python
Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Hello 123</h1>"

import mysql.connector

connection = mysql.connector.connect(user = ‘root’, database = ‘elite_102’, password = "Nafisa@2008")

connection.close()

cursor = connection.cursor()

testQuery = (“SELECT * FROM student”)

cursor.execute(testQuery)
cursor.close()
connection.close()
import mysql.connector
from typing import Tuple, TypedDict

credentials = {
    "user": "root",
    "database": "bank",
    "password": "northkoreabestkorea"
}

connection = mysql.connector.connect(**credentials)
connection.autocommit = False

class UserSchema(TypedDict):
    id: int
    username: str
    password: str
    balance: float
    admin: int

#Execute a raw query
def execute(querytext: str, params = tuple()) -> Tuple[bool, list[tuple] | str]:
    try:
        cursor = connection.cursor()

        cursor.execute(querytext, params)

        data = [x for x in cursor]

        cursor.close()
        return (True, data)
    except Exception as err:
        cursor.close()
        return (False, err)
    
#Execute a select query
def query(querytest: str, params = tuple()) -> Tuple[bool, list[tuple] | str]:
    result = execute(querytest, params)

    #If query fails, return err as is
    #Otherwise, return structured data
    if not result[0]:
        return result
    else:
        return (True, [structure(x) for x in result[1]])
    

#Turn tuples returned by MySQL into a dictionary
def structure(raw: tuple) -> UserSchema:
    keys = ["id", "username", "password", "balance", "admin"]

    #Assign each tupe value to a key
    dictionary = dict(
        zip(keys, list(raw))
    )

    #Replease 1/0 booleans with Python booleans
    if dictionary["admin"] == 1:
        dictionary["admin"] = True
    else:
        dictionary["admin"] = False

    return dictionary

def register(username: str, password: str) -> bool:
    result = db.execute(f'insert into users (username, password, balance, admin) values (%s, %s, 0, false);', (username, password))
    print(result)

    db.connection.commit()
    return result[0]

#Login to an account
def login(username: str, password: str) -> bool:
    #Find the user trying to log in
    user = db.query("select * from users where username=%s", (username,))
    print(user)

    #Error or nonexistent user
    if not user[0] or len(user[1]) < 1:
        return False
    else:
        return password == user[1][0]["password"]

#Get user ID from username
def getid(username: str) -> int:
    user = db.query("select * from users where username=%s", (username,))
    
    #Error or no user found
    if not user[0] or len(user[1]) < 1:
        return -1
    else:
        return user[1][0]["id"]

#Delete account
def delete_account(username: int, password: str) -> bool:
    #make sure user is authenticated to delete account
    if not login(username, password):
        return False
    
    q = db.execute("delete from users where username=%s", (username,))
    db.connection.commit()

    return q[0]

#Change username
def change_username(uid: int, newname: str, password: str) -> bool:
    pass

def change_password(uid: int, oldpass: str, newpass: str) -> bool:
    pass

#Check balance
def balance(uid: int) -> float:
    pass

#Desposit money
def deposit(uid: int, amount: float) -> None:
    pass

#Withdraw money
def withdraw(uid: int, amount: float) -> bool:
    pass

#Wire money between accounts
def wire(sender: int, recipient: int, amount: float) -> bool:
    s = withdraw(sender, amount)
    r = deposit(recipient, amount)

    return s and r

