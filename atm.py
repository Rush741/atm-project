import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="awgar@47",
    database="atm_db"
)


cursor = conn.cursor()

def login():
    print("^^^^^  Welcome to Rush Bank   ^^^^^^")
    account_no = int(input("Enter your account number: "))
    pin = int(input("Enter your PIN: "))
    cursor.execute("SELECT * FROM accounts WHERE account_no = %s AND pin = %s", (account_no, pin))
    result = cursor.fetchone()
    if result:
        print("Login successful!")
        return account_no
    else:
        print("Wrong account number or PIN.")
        return None

def check_balance(account_no):
    cursor.execute("SELECT balance FROM accounts WHERE account_no = %s", (account_no,))
    balance = cursor.fetchone()[0]
    print(f"Your balance is: Rs {balance:.2f}")

def deposit(account_no):
    amount = float(input("Enter amount to deposit: "))
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_no = %s", (amount, account_no))
    conn.commit()
    print(f"Rs {amount} deposited successfully.")

def withdraw(account_no):
    amount = float(input("Enter amount to withdraw: "))
    cursor.execute("SELECT balance FROM accounts WHERE account_no = %s", (account_no,))
    balance = cursor.fetchone()[0]
    if amount > balance:
        print("Insufficient balance!")
    else:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_no = %s", (amount, account_no))
        conn.commit()
        print(f"Rs {amount} withdrawn successfully.")

def atm():
    account_no = login()
    if not account_no:
        return

    while True:
        print("\nOptions:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            check_balance(account_no)
        elif choice == '2':
            deposit(account_no)
        elif choice == '3':
            withdraw(account_no)
        elif choice == '4':
            print("Thank you for transacting using the Rush ATM!")
            break
        else:
            print("Invalid option, try again.")

atm()
