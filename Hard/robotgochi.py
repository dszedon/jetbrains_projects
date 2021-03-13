from random import randrange, choice


class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = 100
        self.overheat = 0
        self.skill_level = 0
        self.boredom = 0
        self.win_book = {"user": 0, "robot": 0, "draw": 0}

    def actions(self):
        while True:

            print(
                f"\nAvailable interactions with {self.name}:\nexit – Exit\ninfo – Check the vitals\nrecharge – Recharge\nsleep – Sleep mode\nplay – Play\n"
            )

            action = input("Choose:\n")

            if action == "exit":
                print("Game over.")
                quit()
            elif action == "info":
                print(self.stats())
            elif action == "recharge":
                print(self.recharge())
            elif action == "sleep":
                print(self.sleep())
            elif action == "play":
                self.select_game()
                print(self.end_game())
            else:
                print("\nInvalid input, try again!")

    def stats(self):
        return f"\n{self.name}'s stats are: the battery is {self.battery},\noverheat is {self.overheat},\nskill level is {self.skill_level},\nboredom is {self.boredom}."

    def recharge(self):
        if self.battery == 100:
            return f"{self.name} is charged!"
        else:
            old_battery = self.battery
            old_boredom = self.boredom
            old_overheat = self.overheat

            if self.battery < 91:
                self.battery += 10
            else:
                self.battery = 100
            if self.overheat >= 5:
                self.overheat -= 5
            else:
                self.overheat = 0
            if self.boredom <= 95:
                self.boredom += 5
            else:
                self.boredom = 100

            overheat_msg = f"{self.name}'s level of overheat was {old_overheat}. Now it is {self.overheat}."
            battery_msg = f"{self.name}'s level of the battery was {old_battery}. Now it is {self.battery}."
            boredom_msg = f"{self.name}'s level of boredom was {old_boredom}. Now it is {self.boredom}."
            recharge_msg = f"{self.name} is recharged!"

            return f"{overheat_msg}\n{battery_msg}\n{boredom_msg}\n{recharge_msg}"

    def sleep(self):
        if self.overheat == 0:
            return f"{self.name} is cool!"
        else:
            old_overheat = self.overheat
            if self.overheat <= 19:
                self.overheat = 0
            else:
                self.overheat -= 20

            return f"\n{self.name} cooled off!\n{self.name}'s level of overheat was {old_overheat}. Now it is {self.overheat}."

    def select_game(self):
        while True:
            user_input = input("\nWhich game would you like to play?\n")

            if user_input == "Rock-paper-scissors":
                self.rck_sci_ppr()
                break
            elif user_input == "Numbers":
                self.num_game()
                break
            else:
                print("Please choose a valid option: Numbers or Rock-paper-scissors?")

    def end_game(self):
        old_boredom = self.boredom
        old_overheat = self.overheat

        if self.overheat < 91:
            self.overheat += 10
        else:
            self.overheat = 100
            if self.boredom > 10:
                self.boredom -= 10
            else:
                self.boredom = 0

        boredom_msg = f"{self.name}'s level of boredom was {old_boredom}. Now it is {self.boredom}."
        overheat_msg = f"{self.name}'s level of overheat was {old_overheat}. Now it is {self.overheat}."

        if self.boredom == 0:
            return f"{boredom_msg}\n{overheat_msg}\n{self.name} is in a great mood!"
        else:
            return f"{boredom_msg}\n{overheat_msg}\n"

    def num_game(self):
        goal_num = randrange(0, 1000000)
        robot_num = randrange(0, 1000000)

        while True:
            user_num = input("\nWhat is your number?\n")
            check_response = self.check_user_num(user_num)

            if check_response == "quit":
                print(
                    f"""\nYou won: {self.win_book['user']},
The robot won: {self.win_book['robot']},
Draws: {self.win_book['draw']}.\n"""
                )
                break
            elif check_response != "pass":
                print(check_response)
            else:
                winner = self.check_winner_num(goal_num, user_num, robot_num)

                print(
                    f"""\nThe robot entered the number {robot_num}.
The goal number is {goal_num}."""
                )

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
                print(
                    f"""\nYou won: {self.win_book['user']},
        The robot won: {self.win_book['robot']},
        Draws: {self.win_book['draw']}.\n"""
                )
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
