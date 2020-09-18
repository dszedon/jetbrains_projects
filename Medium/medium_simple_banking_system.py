"""
SIMPLE BANKING SYSTEM

About
Everything goes digital these days, and so does money. Today, most people have credit cards, which save us time, energy and nerves. 
From not having to carry a wallet full of cash to consumer protection, cards make our lives easier in many ways. 
In this project, you will develop a simple banking system with database.

Learning outcomes
In this project, you will find out how the banking system works and learn about SQL.
We'll also see how Luhn algorithm can help us avoid mistakes when entering the card number. 
As an overall result, you'll get new experience in Python.

Stage 1
Find out what a credit card consists of

Stage 2
Implement Luhn Algorithm to check the card number for validity

Stage 3
Create a database and store your data in it

Stage 4
Improve your system by extending its functionality.

"""

import random
import sqlite3


def start():
    while True:
        action = int(
            input(
                """1. Create an account
2. Log into account
0. Exit\n"""
            )
        )
        if action == 0:
            print("Bye!")
            quit()
        elif action == 1:
            create_acc()
        elif action == 2:
            login()


def create_acc():
    verify_card()
    print(
        """\nYour card has been created
Your card number:
{}
Your card PIN:
{}\n""".format(
            card, pin
        )
    )


def verify_card():
    while True:
        card_gen()
        valid = luhn_alg(card)
        if valid % 10 == 0:
            update_db(card, pin)

            break


def card_gen():
    global card
    global pin

    # gen card
    usernum = str(random.randrange(0, 9999999999))
    lencard = len(usernum)
    if lencard < 10:
        usernum = (10 - lencard) * "0" + usernum
    card = "400000" + usernum

    # gen pin
    pin = str(random.randrange(0, 9999))
    lenpin = len(pin)
    if lenpin < 4:
        pin = (4 - lenpin) * "0" + pin


def luhn_alg(cardnum):
    checsum = 0
    count = 0
    for x in cardnum[:15]:
        x = int(x)
        if count % 2 == 0:
            x = x * 2
        if x > 9:
            x = x - 9
        checsum = x + checsum
        count += 1
    checsum = checsum + int(cardnum[15])
    return checsum


def login():
    global db_card
    db_card = ""
    db_pin = ""
    log_card = input("Enter your card number:\n")
    log_pin = input("Enter your PIN:\n")

    cur.execute("SELECT * FROM card")
    accounts = cur.fetchall()

    for item in accounts:
        db_card = str(item[1])
        db_pin = str(item[2])
        if (db_card == log_card) and (db_pin == log_pin):
            account_in()
            break
    if (db_card != log_card) or (db_pin != log_pin):
        print("\nWrong card number or PIN!\n")


def account_in():
    print("\nYou have successfully logged in!\n")

    while True:
        action2 = int(
            input(
                """1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit\n"""
            )
        )
        if action2 == 0:
            print("\nBye!")
            quit()
        elif action2 == 1:
            get_balance(db_card)
        elif action2 == 2:
            add_income(db_card)
        elif action2 == 3:
            transfer(db_card)
        elif action2 == 4:
            close_acc(db_card)
            print("\nThe account has been closed!\n")
            break
        elif action2 == 5:
            print("\nYou have successfully logged out!\n")
            break


def show_db(accountnum):
    cur.execute("SELECT * FROM card")
    accounts = cur.fetchall()
    for i in accounts:
        print(i)


def get_balance(accountnum):
    cur.execute("SELECT * FROM card WHERE number = (?)", (accountnum,))
    accounts = cur.fetchall()
    print("Balance: " + str(accounts[0][3]))


def add_income(accountnum):
    add_money = int(input("Enter income:\n"))

    cur.execute("UPDATE card SET balance = balance + (?) WHERE number = (?)",
                (add_money, accountnum,))
    conn.commit()


def transfer(accountnum):
    print("\nTransfer")
    transfer_acc = str(input("Enter card number:\n"))

    if transfer_acc[0] != "4":
        print("Such a card does not exist.")
    else:
        cur.execute("SELECT * FROM card")
        accounts = cur.fetchall()

        for item in accounts:
            db_card = str(item[1])
            if (db_card == transfer_acc):
                transfer_money(accountnum, transfer_acc)
        if (db_card != transfer_acc):
            print("Probably you made mistake in the card number. Please try again!")


def transfer_money(accountnum, transfer_acc):
    cur.execute("SELECT * FROM card WHERE number = (?)", (accountnum,))
    accounts = cur.fetchall()

    account_balance = int(accounts[0][3])

    transfer_money = int(input("Enter how much money you want to transfer:\n"))

    if transfer_money > account_balance:
        print("Not enough money!")
    else:
        # substract money from first acc
        cur.execute("UPDATE card SET balance = balance - (?) WHERE number = (?)",
                    (transfer_money, accountnum,))
        conn.commit()

        # add money to second acc
        cur.execute("UPDATE card SET balance = balance + (?) WHERE number = (?)",
                    (transfer_money, transfer_acc,))
        conn.commit()

        print("Succes!")


def close_acc(accountnum):
    cur.execute("DELETE FROM card WHERE number = (?)", (accountnum,))
    conn.commit()


def update_db(card, pin):

    row_add = (card, pin)
    cur.execute(
        "INSERT INTO card (number, pin) VALUES(?,?)", row_add)
    conn.commit()


conn = sqlite3.connect("card.s3db")
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS card(
                id INTEGER,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0
)""")

conn.commit()


card = 0
pin = 0
checsum = 0


start()
conn.close()
