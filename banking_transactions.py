import mysql.connector

#function to create database connection
def db_connection():

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="madhav",
      database="banking"
    )
    return mydb


#function to close database connection
def close_dbconnection(db):
      db.close()


# function to create an account
def create_account():
    name = input("Enter Name: ")
    pin = input("Enter pin: ")
    balance = input("enter deposit amount: ")

    mydb = db_connection()
    mycursor = mydb.cursor()

    sql = ("INSERT INTO Account (pin,name, balance) VALUES ( %s, %s, %s)")
    values = (pin, name, balance)
    mycursor.execute(sql, values)

    mydb.commit()
    close_dbconnection(mydb)

    print("Succesfully created an account.Your Account Number is : ",mycursor.lastrowid)
    tmp = input("press enter to continue ")

# function to make a deposit
def deposit():
    acc_number = input("Enter account number: ")
    amount = input("Enter amount: ")

    mydb = db_connection()
    mycursor = mydb.cursor()

    sql = ("INSERT INTO transactions (acc_number,amount,transaction_name) VALUES (%s, %s, %s)")
    values = (acc_number, amount, 'deposit')
    mycursor.execute(sql, values)

    mycursor.execute("select balance from Account where acc_number = " + acc_number + "")

    myresult = mycursor.fetchone()
    acc_balance = myresult[0]
    new_balance = int(acc_balance) + int(amount)
    sql1 = "update Account set balance = %s where acc_number =%s"
    val = (new_balance, acc_number)
    mycursor.execute(sql1, val)
    mydb.commit()
    close_dbconnection(mydb)

    print("Deposit successfull!")


# function to make withdrawal
def withdraw():
    acc_number = input("Enter account number: ")
    amount = input("Enter amount: ")

    mydb = db_connection()
    mycursor = mydb.cursor()

    sql = ("INSERT INTO transactions (acc_number,amount,transaction_name) VALUES (%s, %s, %s)")
    values = (acc_number, amount, 'Withdrawal')
    mycursor.execute(sql, values)

    mycursor.execute("select balance from Account where acc_number = " + acc_number + "")

    myresult = mycursor.fetchone()
    acc_balance = myresult[0]
    new_balance = int(acc_balance) - int(amount)
    sql1 = "update Account set balance = %s where acc_number =%s"
    val = (new_balance, acc_number)

    mycursor.execute(sql1, val)

    mydb.commit()
    close_dbconnection(mydb)

    print("Withdrawal successful!")


# function to check balance
def check_balance():
    acc_number = input("Enter account number: ")

    mydb = db_connection()

    mycursor = mydb.cursor()

    mycursor.execute("select balance from Account where acc_number = " + acc_number + "")

    myresult = mycursor.fetchall()

    close_dbconnection(mydb)

    print("Current balance is : ", myresult[0][0])

    tmp = input("press enter to continue ")


# function to delete account

def delete_account():
    acc_number = int(input("Enter account number: "))

    mydb = db_connection()

    mycursor = mydb.cursor()

    sql1 = ("delete from Account where acc_number = %s")
    values1 = (acc_number,)

    mycursor.execute(sql1, values1)
    sql = ("delete from transactions where acc_number = %s")
    values = (acc_number,)
    mycursor.execute(sql, values)

    mydb.commit()
    close_dbconnection(mydb)
    print("Succesfully deleted account.")
    tmp = input("press enter to continue ")

# function to Modify account details
def modify_account():
    acc_number = input("Enter account number: ")
    name = input("Enter username: ")
    pin = input("Enter pin: ")

    mydb = db_connection()

    mycursor = mydb.cursor()

    sql = ("update Account set pin = %s, name = %s where acc_number = %s")
    values = (pin, name, acc_number)
    mycursor.execute(sql, values)

    mydb.commit()
    close_dbconnection(mydb)
    print("Succesfully modified your account details.")
    tmp = input("press enter to continue ")
