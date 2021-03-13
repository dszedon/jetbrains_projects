from random import randrange, choice

win_book = {"user": 0, "robot": 0, "draw": 0}


class Robot:
    def __init__(self, name):
        self.name = name


def num_game():
    goal_num = randrange(0, 1000000)
    robot_num = randrange(0, 1000000)

    while True:
        user_num = input("What is your number?\n")
        check_response = check_user_num(user_num)

        if check_response == "quit":
            print(
                f"""\nYou won: {win_book['user']},
    The robot won: {win_book['robot']},
    Draws: {win_book['draw']}."""
            )
            quit()
        elif check_response != "pass":
            print(check_response)
        else:
            winner = check_winner_num(goal_num, user_num, robot_num)

            print(
                f"""The robot entered the number {robot_num}.
    The goal number is {goal_num}."""
            )

            if winner == "user":
                print("You won!")

            elif winner == "robot":
                print("The robot won!")


def check_user_num(user_num):
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


def check_winner_num(goal_num, user_num, robot_num):
    user_num = int(user_num)

    if abs(goal_num - robot_num) > abs(goal_num - user_num):
        win_book["user"] += 1
        return "user"
    elif abs(goal_num - robot_num) == abs(goal_num - user_num):
        win_book["draw"] += 1
        return "draw"
    else:
        win_book["robot"] += 1
        return "robot"


def rck_sci_ppr():
    moves = ["Rock", "Scissors", "Paper"]
    while True:

        robot_move = choice(moves)

        user_move = input("What is your move?\n")

        if "exit game" in user_move:
            print(
                f"""\nYou won: {win_book['user']},
    The robot won: {win_book['robot']},
    Draws: {win_book['draw']}."""
            )
            quit()
        else:
            if user_move.capitalize() not in moves:
                print("No such option! Try again!")
            else:
                print(f"The robot chose {robot_move}")
                if user_move.capitalize() == robot_move:
                    win_book["draw"] += 1
                    print("It's a draw!")
                elif user_move.capitalize() == "Rock" and robot_move == "Scissors":
                    win_book["user"] += 1
                    print("You won!")
                elif user_move.capitalize() == "Scissors" and robot_move == "Paper":
                    win_book["user"] += 1
                    print("You won!")
                elif user_move.capitalize() == "Paper" and robot_move == "Rock":
                    win_book["user"] += 1
                    print("You won!")
                else:
                    win_book["robot"] += 1
                    print("The robot won!")


def select_game():
    while True:
        user_input = input("Which game would you like to play?\n")

        if user_input == "Rock-paper-scissors":
            rck_sci_ppr()
        elif user_input == "Numbers":
            num_game()
        else:
            print("Please choose a valid option: Numbers or Rock-paper-scissors?")


# robot_name = intput("How will you call your robot?\n")
robot_name = "Not my robot"


print(
    f"""Available interactions with {robot_name}:
exit - Exit
info - Check the vitals
recharge - Recharge
sleep - Sleep mode
play - Play\n"""
)


# action = input("Choose:\n")
