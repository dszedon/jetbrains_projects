class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = 100
        self.overheat = 0
        self.skill_level = 0
        self.boredom = 0

    def actions(self):
        print(
            f"\nAvailable interactions with {self.name}:\nexit -- Exit\ninfo -- Check the vitals\nrecharge -- Recharge\nsleep -- Sleep mode\nplay -- Play\n"
        )

        while True:
            action = input("Choose:\n")

            if action == "exit":
                quit()
            elif action == "info":
                print("here")
                self.stats()
            elif action == "recharge":
                pass
            elif action == "sleep":
                pass
            elif action == "play":
                pass
            else:
                print("\nInvalid input, try again!")

    def stats(self):
        return f"{self.name}'s stats are: the battery is {self.battery},\noverheat is {self.overheat},\nskill level is {self.skill_level},\nboredom is {self.boredom}."

    def select_game(self):
        while True:
            user_input = input("Which game would you like to play?\n")

            if user_input == "Rock-paper-scissors":
                # rck_sci_ppr()
                pass
            elif user_input == "Numbers":
                # num_game()
                pass
            else:
                print("Please choose a valid option: Numbers or Rock-paper-scissors?")


robo = Robot("Daniel")

print(robo.name)
robo.actions()
