"""

Cofee Machine

About
What can be better than a cup of coffee during a break? A coffee that you don’t have to make yourself. 
It’s enough to press a couple of buttons on the machine and you get a cup of energy; but first, we should teach the machine how to do it. 
In this project, you will work on programming a coffee machine simulator. 
The machine works with typical products: coffee, milk, sugar, and plastic cups; if it runs out of something, it shows a notification. 
You can get three types of coffee: espresso, cappuccino, and latte. Since nothing’s for free, it also collects the money.

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
