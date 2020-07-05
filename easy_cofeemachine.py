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
class CoffeeType:
    def __init__(self, ingredients):
        self.water = ingredients[0]
        self.milk = ingredients[1]
        self.beans = ingredients[2]
        self.money = ingredients[3]
        self.cups = ingredients[4]


class CoffeeMachine:
    def __init__(self, stocks):
        self.water = stocks[0]
        self.milk = stocks[1]
        self.beans = stocks[2]
        self.cups = stocks[3]
        self.money = stocks[4]
        self.espresso = CoffeeType([250, 0, 16, -4, 1])
        self.latte = CoffeeType([350, 75, 20, -7, 1])
        self.cappuccino = CoffeeType([200, 100, 12, -6, 1])

    def start(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit):')
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.stock()
            elif action == 'exit':
                break

    def buy(self):
        coffee = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
        if coffee == '1':
            self.make_coffee(self.espresso)
        elif coffee == '2':
            self.make_coffee(self.latte)
        elif coffee == '3':
            self.make_coffee(self.cappuccino)

    def fill(self):
        in_water = int(input('\nWrite how many ml of water do you want to add:\n'))
        self.water += in_water
        in_milk = int(input('Write how many ml of milk do you want to add:\n'))
        self.milk += in_milk
        in_beans = int(input('Write how many grams of coffee beans do you want to add:\n'))
        self.beans += in_beans
        in_cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))
        self.cups += in_cups

    def take(self):
        print('\nI gave you $' + str(self.money))
        self.money = 0

    def stock(self):
        print('\nThe coffee machine has: ')
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.beans) + ' of coffee beans')
        print(str(self.cups) + ' of disposable cups')
        print('$' + str(self.money) + ' of money\n')

    def make_coffee(self, coffee):
        if (self.water // coffee.water) < 1:
            print('Sorry, not enough water!\n')
        elif coffee.milk != 0 and (self.milk // coffee.milk) < 1:
            print('Sorry, not enough milk!\n')
        elif (self.beans // coffee.beans) < 1:
            print('Sorry, not enough coffee beans!\n')
        elif (self.cups // coffee.cups) < 1:
            print('Sorry, not enough disposable cups!\n')
        else:
            print('I have enough resources, making you a coffee!\n')
            self.water -= coffee.water
            self.milk -= coffee.milk
            self.beans -= coffee.beans
            self.money -= coffee.money
            self.cups -= coffee.cups


water = 400
milk = 540
beans = 120
cups = 9
money = 550
rocket = CoffeeMachine([water, milk, beans, cups, money])
rocket.start()
