"""
Description

Let's redesign our program and write a class that represents the coffee machine. 
The class should have a method that takes a string as input. 
Every time the user inputs a string to the console, the program invokes this method with one argument: 
the line that user input to the console. This system simulates pretty accurately how real-world electronic devices work. 
External components (like buttons on the coffee machine or tapping on the screen) generate events that pass into the single interface of the program.

The class should not use system input at all; 
it will only handle the input that comes to it via this method and its string argument.

The first problem that comes to mind: 
how to write that method in a way that it represents all that coffee machine can do? 
If the user inputs a single number, how can the method determine what that number is: 
a variant of coffee chosen by the user or the number of the disposable cups that a special worker added into the coffee machine?

The right solution to this problem is to store the current state of the machine. 
The coffee machine has several states it can be in. 
For example, the state could be "choosing an action" or "choosing a type of coffee". 
Every time the user inputs something and a program passes that line to the method, 
the program determines how to interpret this line using the information about the current state. 
After processing this line, the state of the coffee machine can be changed or can stay the same.

Objective

Your final task is to refactor the program. 
Make it so that you can communicate with the coffee machine through a single method. 
Good luck!

"""

class CoffeeMachine:
 
    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
 
    def status_judge(self, water_change, milk_change, beans_change, cups_change, money_change):
        if self.water + water_change < 0:
            print("Sorry, not enough water!")
            return False
        elif self.milk + milk_change < 0:
            print("Sorry, not enough milk!")
            return False
        elif self.beans + beans_change < 0:
            print("Sorry, not enough beans!")
            return False
        elif self.cups + cups_change < 0:
            print("Sorry, not enough cups!")
            return False
        else:
            return True
 
    def status_changes(self, water_change, milk_change, beans_change, cups_change, money_change):
        self.water = self.water + water_change
        self.milk = self.milk + milk_change
        self.beans = self.beans + beans_change
        self.cups = self.cups + cups_change
        self.money = self.money + money_change
 
    def status_show(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")
 
    def buy(self):
        coffee_choice = input("What do you want to buy? 1 - espresso, 2 - latte, "
                              "3 - cappuccino, back - to main menu:")
        if coffee_choice == '1':
            if self.status_judge(-250, 0, -16, -1, 4):
                print("I have enough resources, making you a coffee!")
                self.status_changes(-250, 0, -16, -1, 4)
        elif coffee_choice == '2':
            if self.status_judge(-350, -75, -20, -1, 7):
                print("I have enough resources, making you a coffee!")
                self.status_changes(-350, -75, -20, -1, 7)
        elif coffee_choice == '3':
            if self.status_judge(-200, -100, -12, -1, 6):
                print("I have enough resources, making you a coffee!")
                self.status_changes(-200, -100, -12, -1, 6)
 
    def fill(self):
        water_fill = int(input("Write how many ml of water do you want to add:").strip())
        milk_fill = int(input("Write how many ml of milk do you want to add:"))
        beans_fill = int(input("Write how many grams of coffee beans do you want to add:"))
        cups_fill = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.status_changes(water_fill, milk_fill, beans_fill, cups_fill, 0)
 
    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0
 
    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.status_show()
            elif action == "exit":
                break
 
 
test = CoffeeMachine()
test.start()
"""
class CoffeeMachine:
 
    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
 
    def status_judge(self, water_change, milk_change, beans_change, cups_change, money_change):
        if self.water + water_change < 0:
            print("Sorry, not enough water!")
            return False
        elif self.milk + milk_change < 0:
            print("Sorry, not enough milk!")
            return False
        elif self.beans + beans_change < 0:
            print("Sorry, not enough beans!")
            return False
        elif self.cups + cups_change < 0:
            print("Sorry, not enough cups!")
            return False
        else:
            return True
 
    def status_changes(self, water_change, milk_change, beans_change, cups_change, money_change):
        self.water = self.water + water_change
        self.milk = self.milk + milk_change
        self.beans = self.beans + beans_change
        self.cups = self.cups + cups_change
        self.money = self.money + money_change
 
    def status_show(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")
 
    def buy(self):
        coffee_choice = input("What do you want to buy? 1 - espresso, 2 - latte, "
                              "3 - cappuccino, back - to main menu:")
        if coffee_choice == '1':
            if self.status_judge(-250, 0, -16, -1, 4):
                print("I have enough resources, making you a coffee!")
                self.status_changes(-250, 0, -16, -1, 4)
        elif coffee_choice == '2':
            if self.status_judge(-350, -75, -20, -1, 7):
                print("I have enough resources, making you a coffee!")
                self.status_changes(-350, -75, -20, -1, 7)
        elif coffee_choice == '3':
            if self.status_judge(-200, -100, -12, -1, 6):
                print("I have enough resources, making you a coffee!")
                self.status_changes(-200, -100, -12, -1, 6)
 
    def fill(self):
        water_fill = int(input("Write how many ml of water do you want to add:").strip())
        milk_fill = int(input("Write how many ml of milk do you want to add:"))
        beans_fill = int(input("Write how many grams of coffee beans do you want to add:"))
        cups_fill = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.status_changes(water_fill, milk_fill, beans_fill, cups_fill, 0)
 
    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0
 
    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.status_show()
            elif action == "exit":
                break
 
 
test = CoffeeMachine()
test.start()
