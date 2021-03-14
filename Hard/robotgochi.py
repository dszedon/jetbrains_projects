from random import randrange, choice


class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = 100
        self.overheat = 0
        self.skill_level = 0
        self.boredom = 0
        self.rust = 0
        self.win_book = {"user": 0, "robot": 0, "draw": 0}

    def alert_msg(self):
        self.skill_msg = f"{self.name}'s level of skill was {self.old_skill}. Now it is {self.skill_level}."
        self.battery_msg = f"{self.name}'s level of the battery was {self.old_battery}. Now it is {self.battery}."
        self.overheat_msg = f"{self.name}'s level of overheat was {self.old_overheat}. Now it is {self.overheat}."
        self.boredom_msg = f"{self.name}'s level of boredom was {self.old_boredom}. Now it is {self.boredom}."
        self.rust_msg = (
            f"{self.name}'s level of rust was {self.old_rust}. Now it is {self.rust}."
        )

    def old_values(self):
        self.old_skill = self.skill_level
        self.old_battery = self.battery
        self.old_overheat = self.overheat
        self.old_boredom = self.boredom
        self.old_rust = self.rust

    def check_vitals(self):
        if self.battery == 0:
            return f"The level of the battery is 0, {self.name} needs recharging!"
        elif self.boredom == 100:
            return f"{self.name} is too bored! {self.name} needs to have fun!"
        elif self.overheat == 100:
            return f"The level of overheat reached 100, {self.name} has blown up! Game over. Try again?"
        elif self.rust == 100:
            return f"{self.name} is too rusty! Game over. Try again?"
        else:
            return "none"

    def unpleasent_event(self):

        event = choice(["puddle", "sprinkler", "pool", "none"])

        if event == "puddle":
            self.rust = 100 if self.rust >= 90 else self.rust + 10
            return f"Oh no, {self.name} stepped into a puddle!"
        elif event == "sprinkler":
            self.rust = 100 if self.rust >= 70 else self.rust + 30
            return f"Oh, {self.name} encountered a sprinkler!."
        elif event == "pool":
            self.rust = 100 if self.rust >= 50 else self.rust + 50
            return f"Guess what! {self.name} fell into the pool!"
        else:
            return "none"

    def actions(self):
        while True:

            print(f"\nAvailable interactions with {self.name}:")
            print("exit – Exit")
            print("info – Check the vitals")
            print("work – Work")
            print("play – Play")
            print("oil – Oil")
            print("recharge – Recharge")
            print("sleep – Sleep mode")
            print("learn – Learn skills\n")

            action = input("Choose:\n")

            vitals = self.check_vitals()

            condition_battery = "battery" in vitals and action != "recharge"
            condition_bored = "bored" in vitals and action != "play"
            condition_overheat = "overheat" in vitals and action != "sleep"

            if condition_battery is True or condition_bored is True:
                print(f"\n{vitals}")
                continue
            elif condition_overheat is True:
                print(f"\n{vitals}")
                quit()

            if action == "exit":
                print("\nGame over.")
                quit()
            elif action == "info":
                print(self.stats())
            elif action == "work":
                print(self.work())
            elif action == "play":
                self.select_game()
                print(self.end_game())
            elif action == "oil":
                print(self.oil())
            elif action == "recharge":
                print(self.recharge())
            elif action == "sleep":
                print(self.sleep())
            elif action == "learn":
                print(self.learn())
            else:
                print("\nInvalid input, try again!")

    def stats(self):
        return f"\n{self.name}'s stats are: the battery is {self.battery},\noverheat is {self.overheat},\nskill level is {self.skill_level},\nboredom is {self.boredom},\nrust level is {self.rust}."

    def work(self):

        if self.skill_level < 50:
            return f"\n{self.name} has got to learn before working!"
        else:
            self.old_values()

            self.battery = 0 if self.battery <= 10 else self.battery - 10
            self.overheat = 100 if self.overheat >= 90 else self.overheat + 10
            self.boredom = 100 if self.boredom >= 90 else self.boredom + 10

            event_msg = self.unpleasent_event()

            vitals = self.check_vitals()

            if "rusty" in vitals:
                print(vitals)
                quit()

            self.alert_msg()

            event_txt = f"\n{event_msg}\n\n{self.boredom_msg}\n{self.overheat_msg}\n{self.battery_msg}\n{self.rust_msg}\n\n{self.name} did well!"
            no_event_txt = f"\n{self.boredom_msg}\n{self.overheat_msg}\n{self.battery_msg}\n\n{self.name} did well!"

            return no_event_txt if event_msg == "none" else event_txt

    def oil(self):
        if self.rust == 0:
            return f"\n{self.name} is fine, no need to oil!"
        else:
            self.rust = 0 if self.rust <= 20 else self.rust - 20
            return f"\n{self.rust_msg}\n{self.name} is less rusty!"

    def recharge(self):
        if self.battery == 100:
            return f"{self.name} is charged!"
        else:
            self.old_values()

            self.battery = 100 if self.battery >= 90 else self.battery + 10
            self.overheat = 0 if self.overheat <= 5 else self.overheat - 5
            self.boredom = 100 if self.boredom >= 95 else self.boredom + 5

            self.alert_msg()
            recharge_msg = f"{self.name} is recharged!"

            return f"\n{self.overheat_msg}\n{self.battery_msg}\n{self.boredom_msg}\n\n{recharge_msg}"

    def sleep(self):
        if self.overheat == 0:
            return f"{self.name} is cool!"
        else:
            self.old_values()

            self.overheat = 0 if self.overheat < 20 else self.overheat - 20

            self.alert_msg()

            return f"\n{self.overheat_msg}\n\n{self.name} cooled off!"

    def learn(self):
        if self.skill_level == 100:
            return f"There's nothing for {self.name} to learn!"
        else:
            self.old_values()
            self.skill_level += 10
            self.battery -= 10
            self.overheat += 10
            self.boredom += 5

            self.alert_msg()

            return f"\n{self.skill_msg}\n{self.overheat_msg}\n{self.battery_msg}\n{self.boredom_msg}\n\n{self.name} has become smarter!"

    def select_game(self):
        while True:
            user_input = input("\nWhich game would you like to play?\n")

            if user_input.capitalize() == "Rock-paper-scissors":
                self.rck_sci_ppr()
                break
            elif user_input.capitalize() == "Numbers":
                self.num_game()
                break
            else:
                print("Please choose a valid option: Numbers or Rock-paper-scissors?")

    def end_game(self):
        self.old_values()

        event_msg = self.unpleasent_event()

        vitals = self.check_vitals()

        if "rusty" in vitals:
            print(vitals)
            quit()

        self.overheat = 100 if self.overheat >= 95 else self.overheat + 5
        self.boredom = 0 if self.boredom <= 10 else self.boredom - 10

        self.alert_msg()

        if self.boredom == 0:
            event_txt = f"{event_msg}\n\n{self.rust_msg}\n{self.overheat_msg}\n{self.boredom_msg}\n{self.name} is in a great mood!"
            no_event_txt = f"{self.overheat_msg}\n{self.boredom_msg}\n{self.name} is in a great mood!"
        else:
            event_txt = f"{event_msg}\n\n{self.rust_msg}\n\n{self.overheat_msg}{self.boredom_msg}"
            no_event_txt = f"\n{self.overheat_msg}{self.boredom_msg}"

        return no_event_txt if event_msg == "none" else event_txt

    def num_game(self):
        goal_num = randrange(0, 1000000)
        robot_num = randrange(0, 1000000)

        while True:
            user_num = input("\nWhat is your number?\n")
            check_response = self.check_user_num(user_num)

            if check_response == "quit":
                print(f"\nYou won: {self.win_book['user']},")
                print(f"The robot won: {self.win_book['robot']},")
                print(f"Draws: {self.win_book['draw']}.\n")
                break
            elif check_response != "pass":
                print(check_response)
            else:
                winner = self.check_winner_num(goal_num, user_num, robot_num)

                print(f"\nThe robot entered the number {robot_num}.")
                print(f"The goal number is {goal_num}.")

                if winner == "user":
                    print("You won!")

                elif winner == "robot":
                    print("The robot won!")

    def check_user_num(self, user_num):
        if user_num == "exit game":
            return "quit"
        else:
            try:
                user_num = int(user_num)

                if user_num > 1000000:
                    return "Invalid input! The number can't be bigger than 1000000."
                elif user_num < 0:
                    return "The number can't be negative!"
                else:
                    return "pass"

            except Exception:
                return "A string is not a valid input!"

    def check_winner_num(self, goal_num, user_num, robot_num):
        user_num = int(user_num)

        if abs(goal_num - robot_num) > abs(goal_num - user_num):
            self.win_book["user"] += 1
            return "user"
        elif abs(goal_num - robot_num) == abs(goal_num - user_num):
            self.win_book["draw"] += 1
            return "draw"
        else:
            self.win_book["robot"] += 1
            return "robot"

    def rck_sci_ppr(self):
        moves = ["Rock", "Scissors", "Paper"]
        while True:

            robot_move = choice(moves)

            user_move = input("\nWhat is your move?\n")

            if "exit game" in user_move:
                print(f"\nYou won: {self.win_book['user']},")
                print(f"The robot won: {self.win_book['robot']},")
                print(f"Draws: {self.win_book['draw']}.\n")
                break
            else:
                if user_move.capitalize() not in moves:
                    print("\nNo such option! Try again!")
                else:
                    print(f"\nThe robot chose {robot_move}")
                    if user_move.capitalize() == robot_move:
                        self.win_book["draw"] += 1
                        print("It's a draw!")
                    elif user_move.capitalize() == "Rock" and robot_move == "Scissors":
                        self.win_book["user"] += 1
                        print("You won!")
                    elif user_move.capitalize() == "Scissors" and robot_move == "Paper":
                        self.win_book["user"] += 1
                        print("You won!")
                    elif user_move.capitalize() == "Paper" and robot_move == "Rock":
                        self.win_book["user"] += 1
                        print("You won!")
                    else:
                        self.win_book["robot"] += 1
                        print("The robot won!")


robo_name = input("How will you call your robot?\n")
robo = Robot(robo_name)
robo.actions()
