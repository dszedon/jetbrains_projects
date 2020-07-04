"""
cofee machine
"""

def esp():
    # needs 250 ml of water and 16 g of coffee beans. It costs $4.
    global w, c, mo, dc
    if (w > 250) and (c > 16) and (dc > 1):
        w = w - 250
        c = c - 16
        mo = mo + 4
        dc = dc - 1
    else:
        if (w < 250):
            print("Sorry, not enough water!")
        elif (c < 16):
            print("Sorry, not enough cofee!")
        elif (dc < 1):
            print("Sorry, not enough disposable cups!")


def latt():
    # needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
    global w, m, c, mo, dc
    if (w > 350) and (m > 75) and (c > 20) and (dc > 1):
        w = w - 350
        m = m - 75
        c = c - 20
        mo = mo + 7
        dc = dc - 1
    else:
        if (w < 350):
            print("Sorry, not enough water!")
        elif (m < 750):
            print("Sorry, not enough milk!")
        elif (c < 20):
            print("Sorry, not enough cofee!")
        elif (dc < 1):
            print("Sorry, not enough disposable cups!")


def cap():
    # needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.
    global w, m, c, mo, dc
    if (w >= 200) and (m >= 100) and (c >= 12) and (dc >= 1):
        w = w - 200
        m = m - 100
        c = c - 12
        mo = mo + 6
        dc = dc - 1
    else:
        if (w < 200):
            print("Sorry, not enough water!")
        elif (m < 100):
            print("Sorry, not enough milk!")
        elif (c < 12):
            print("Sorry, not enough cofee!")
        elif (dc < 1):
            print("Sorry, not enough disposable cups!")


def buy():
    buying = input(
        "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if (buying == "1") or (buying == "espresso"):
        esp()
    elif (buying == "2") or (buying == "latte"):
        latt()
    elif (buying == "3") or (buying == "cappuccino"):
        cap()
    elif (buying == "back"):
        pass
    print("I have enough resources, making you a coffee!")


def fill():
    global w, m, c, dc, mo
    global in_w, in_m, in_c, in_dc
    in_w = int(input("Write how many ml of water do you want to add:"))
    in_m = int(input("Write how many ml of milk do you want to add:"))
    in_c = int(input("Write how many grams of coffee beans do you want to add:"))
    in_dc = int(
        input("Write how many disposable cups of coffee do you want to add:"))
    w = w + in_w
    m = m + in_m
    c = c + in_c
    dc = dc + in_dc


def take():
    global mo
    print("I gave you ${}".format(mo))
    mo = 0


def remaining():
    global w, m, c, dc, mo
    print("""The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money""".format(w, m, c, dc, mo))


w = 400
m = 540
c = 120
dc = 9
mo = 550

while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "buy":
        buy()

    elif action == "fill":
        fill()

    elif action == "take":
        take()

    elif action == "remaining":
        remaining()

    elif action == "exit":
        break
