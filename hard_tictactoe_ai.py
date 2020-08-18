"""
TIK TAK TOE AI

About
Everybody remembers this paper-and-pencil game from childhood: 
Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os. 
A single mistake usually costs you the game, but thankfully it is simple enough that most players discover the best strategy quickly. 
Let’s program Tic-Tac-Toe and get playing!

Learning outcomes
After finishing this project, you'll get to know a lot about planning and developing a complex program from scratch, using classes and functions, 
handling errors, and processing user input. 
You will also learn to use OOP (Object-Oriented Programming) in the process.

Stage 1
Learn how to work with the field and the coordinates. 

Stage 2
Make an easy difficulty level where the computer just makes random moves: 
simple to make and not too challenging to beat. 

Stage 3
Whether you want to play with a friend or take a break and watch computers battle it out, you can do both! 

Stage 4
Let’s create a medium difficulty level. 
This AI should be a lot harder to beat! Are you up to the challenge? 

Stage 5
Oh no, what have we created here? 
An unbeatable AI monster! Indeed, this complex algorithm guarantees a win or a draw. 


TODO:
-algorithm for hard mode
-re do medium mode
"""

from random import choice


def game_matrix():

    first_cells = "_________"

    first_cells = first_cells.replace("_", " ")

    occupied_cells = [
        list(first_cells[:3]),
        list(first_cells[3:6]),
        list(first_cells[6:]),
    ]

    return occupied_cells


def print_game_board(occupied_cells):

    aa = occupied_cells[0][0]
    ab = occupied_cells[0][1]
    ac = occupied_cells[0][2]
    ba = occupied_cells[1][0]
    bb = occupied_cells[1][1]
    bc = occupied_cells[1][2]
    ca = occupied_cells[2][0]
    cb = occupied_cells[2][1]
    cc = occupied_cells[2][2]

    game_board = """---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(
        aa, ab, ac, ba, bb, bc, ca, cb, cc
    )

    print(game_board)


def player_move(occupied_cells, player):

    if player == "p1":
        mark = "X"
    else:
        mark = "O"

    while True:
        user = input("Enter the coordinates:").split()

        if user[0].isalpha() is True or user[1].isalpha() is True:
            print("You should enter numbers!")
        elif (int(user[0]) > 3) or (int(user[1]) > 3):
            print("Coordinates should be from 1 to 3!")
        else:

            user = [int(x) - 1 for x in user]
            user[1] = abs(user[1] - 2)

            if occupied_cells[user[1]][user[0]] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                occupied_cells[user[1]][user[0]] = mark
                break

    return occupied_cells


def computer_move(occupied_cells, lvl, player):
    options = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]

    if player == "p1":
        mark = "X"
    else:
        mark = "O"

    if lvl == "easy":

        while True:

            computer_choice = choice(options)

            if (
                occupied_cells[int(computer_choice[0])][int(computer_choice[1])] == "X"
                or occupied_cells[int(computer_choice[0])][int(computer_choice[1])]
                == "O"
            ):
                pass

            else:
                occupied_cells[int(computer_choice[0])][int(computer_choice[1])] = mark
                print('Making move level "{}"'.format(lvl))
                break

        return occupied_cells

    elif lvl == "medium":

        while True:

            if (
                occupied_cells[int(computer_choice[0])][int(computer_choice[1])] == "X"
                or occupied_cells[int(computer_choice[0])][int(computer_choice[1])]
                == "O"
            ):
                pass

            else:
                occupied_cells[int(computer_choice[0])][int(computer_choice[1])] = mark
                print('Making move level "{}"'.format(lvl))
                break

        return occupied_cells

    elif lvl == "hard":
        while True:

            if (
                occupied_cells[int(computer_choice[0])][int(computer_choice[1])] == "X"
                or occupied_cells[int(computer_choice[0])][int(computer_choice[1])]
                == "O"
            ):
                pass

            else:
                occupied_cells[int(computer_choice[0])][int(computer_choice[1])] = mark
                print('Making move level "{}"'.format(lvl))
                break

        return occupied_cells


def minimax():
    pass


def check_winning(occupied_cells):
    free_cells = 9

    options = ["X", "O"]

    try:
        # CHECK FOR DIAGONALS
        for x in options:
            if (
                occupied_cells[0][0] == x
                and occupied_cells[1][1] == x
                and occupied_cells[2][2] == x
            ):
                raise Exception
            elif (
                occupied_cells[0][2] == x
                and occupied_cells[1][1] == x
                and occupied_cells[2][0] == x
            ):
                raise Exception

    except Exception:
        win = "X" if x == "X" else "O"
        print("{} wins".format(win))
        return "gameover"

    else:
        try:
            # CHECK FOR COLUMNS OR ROWS
            for x in options:
                for i in range(0, 3):
                    # COL
                    if (
                        occupied_cells[0][i] == x
                        and occupied_cells[1][i] == x
                        and occupied_cells[2][i] == x
                    ):
                        raise Exception
                    # ROWS
                    elif (
                        occupied_cells[i][0] == x
                        and occupied_cells[i][1] == x
                        and occupied_cells[i][2] == x
                    ):
                        raise Exception
        except Exception:
            win = "X" if x == "X" else "O"
            print("{} wins".format(win))
            return "gameover"

        else:
            # CHECK FOR DRAW
            try:
                for i in range(0, 3):
                    for j in range(0, 3):
                        if occupied_cells[i][j] == "X" or occupied_cells[i][j] == "O":
                            free_cells -= 1
                if free_cells == 0:
                    raise Exception
            except Exception:
                print("Draw")
                return "gameover"


def check_command(command):

    if "exit" in command:
        quit()
    elif len(command) < 3:
        print("Bad parameters!")
        return "ERROR"
    elif command.count("user") == 2 and "start" in command:
        return "PVP"
    elif command.count("easy") == 2 and "start" in command:
        return "CVC"
    elif command.count("medium") == 2 and "start" in command:
        return "CVC"
    elif command.count("hard") == 2 and "start" in command:
        return "CVC"
    elif "medium" in command and "easy" in command and "start" in command:
        return "CVC"
    elif "easy" in command and "user" in command and "start" in command:
        return "PVC"
    elif "medium" in command and "user" in command and "start" in command:
        return "PVC"
    elif "hard" in command and "user" in command and "start" in command:
        return "PVC"
    elif "hard" in command and "easy" in command and "start" in command:
        return "CVC"
    elif "medium" in command and "hard" in command and "start" in command:
        return "CVC"
    else:
        return "NO"


def new_game():

    while True:

        command = str(input("Input command: ")).split()

        try:
            check = check_command(command)

            if check == "ERROR":
                raise Exception
            elif check == "NO":
                pass
            else:
                occupied_cells = game_matrix()
                print_game_board(occupied_cells)

        except Exception:
            pass

        else:

            if check == "PVP":
                player_v_player(occupied_cells)

            elif check == "CVC":
                comp_v_comp(occupied_cells, command[1], command[2])

            elif check == "PVC":

                if "easy" in command:
                    lvl_index = int(command.index("easy"))
                elif "medium" in command:
                    lvl_index = int(command.index("medium"))
                elif "hard" in command:
                    lvl_index = int(command.index("hard"))

                player_v_comp(occupied_cells, command[lvl_index])


def player_v_player(occupied_cells):
    while True:
        try:
            occupied_cells = player_move(occupied_cells, player="p1")
            print_game_board(occupied_cells)
            if check_winning(occupied_cells) == "gameover":
                raise Exception
        except Exception:
            break
        else:
            try:
                occupied_cells = player_move(occupied_cells, player="p2")
                print_game_board(occupied_cells)
                if check_winning(occupied_cells) == "gameover":
                    raise Exception
            except Exception:
                break


def player_v_comp(occupied_cells, lvl):
    while True:
        try:
            occupied_cells = player_move(occupied_cells, player="p1")
            print_game_board(occupied_cells)
            if check_winning(occupied_cells) == "gameover":
                raise Exception
        except Exception:
            break
        else:
            try:
                occupied_cells = computer_move(occupied_cells, lvl, player="p2")
                print_game_board(occupied_cells)
                if check_winning(occupied_cells) == "gameover":
                    raise Exception
            except Exception:
                break


def comp_v_comp(occupied_cells, lvl1, lvl2):
    while True:
        try:
            occupied_cells = computer_move(occupied_cells, lvl1, player="p1")
            print_game_board(occupied_cells)
            if check_winning(occupied_cells) == "gameover":
                raise Exception
        except Exception:
            break
        else:
            try:
                occupied_cells = computer_move(occupied_cells, lvl2, player="p2")
                print_game_board(occupied_cells)
                if check_winning(occupied_cells) == "gameover":
                    raise Exception
            except Exception:
                break


def stop_winning(occupied_cells):

    array = ["X", "O"]

    for x in array:
        # ROWS
        if occupied_cells[0][0] == x and occupied_cells[0][1] == x:
            return "02"
        elif occupied_cells[1][0] == x and occupied_cells[1][1] == x:
            return "12"
        elif occupied_cells[2][0] == x and occupied_cells[2][1] == x:
            return "22"
        elif occupied_cells[0][2] == x and occupied_cells[0][1] == x:
            return "00"
        elif occupied_cells[1][2] == x and occupied_cells[1][1] == x:
            return "10"
        elif occupied_cells[2][2] == x and occupied_cells[2][1] == x:
            return "20"

        # COL
        elif occupied_cells[0][0] == x and occupied_cells[1][0] == x:
            return "20"
        elif occupied_cells[0][1] == x and occupied_cells[1][1] == x:
            return "21"
        elif occupied_cells[0][2] == x and occupied_cells[1][2] == x:
            return "22"
        elif occupied_cells[2][0] == x and occupied_cells[1][0] == x:
            return "00"
        elif occupied_cells[2][1] == x and occupied_cells[1][1] == x:
            return "01"
        elif occupied_cells[2][2] == x and occupied_cells[1][2] == x:
            return "02"

        #  DIAGONALS
        elif occupied_cells[0][0] == x and occupied_cells[1][1] == x:
            return "22"
        elif occupied_cells[2][2] == x and occupied_cells[1][1] == x:
            return "00"
        elif occupied_cells[0][2] == x and occupied_cells[1][1] == x:
            return "20"
        elif occupied_cells[2][0] == x and occupied_cells[1][1] == x:
            return "02"
        elif occupied_cells[0][0] == x and occupied_cells[2][2] == x:
            return "11"
        elif occupied_cells[0][2] == x and occupied_cells[2][0] == x:
            return "11"
        else:
            return "pass"


new_game()
