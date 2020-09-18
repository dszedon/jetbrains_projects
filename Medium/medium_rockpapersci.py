"""
ROCKET SCISSORS PAPER

About
If you’ve ever wanted to create games, this project will get you started! 
In this project you will code a Rock-Paper-Scissors-Lizard-Spock game, a more advanced version of Rock-Paper-Scissors, which can be played against the computer.

Learning outcomes
A playable Rock-Paper-Scissors game, with a Player vs Computer mode. 
Practice using arrays, the Random library, formatted strings, and algorithms.

Stage 1
Before learning how to play the game properly, 
let’s learn how to cheat! Using conditional statements, 
you’ll write a program that always defeats the human player in the Rock-Paper-Scissors game.

Stage 2
Let’s not mess with the player too much, though: from now on, we’re going to play fair. 
You’ll be able to do this with the help of the random module, while string formatting will assist you in announcing the end result of the game.

Stage 3
Can’t stop, won’t stop! A single game is never enough. 
Learn about loops in Python and apply them to make multiple game rounds possible.

Stage 4
It’s time to find out who the best Rock-Paper-Scissors player is! 
You are going to need the basics of file handling to read the records of the results of previous games, as well as tally the user’s score in the current game.

Stage 5
Let's raise the stakes, shall we? In the final stage of the project, 
your program will let the player choose what options will be used in the game and how many of them will be there. 
This will require some more advanced knowledge about lists in Python.

"""
import math
import random


def file_reading():
    global dic
    file = open("rating.txt", "r")
    #file = open("/Users/dsalzedo/Desktop/rating.txt", "r")
    ratings_file = file.readlines()
    dic = {}
    for line in ratings_file:
        dic[line.split()[0]] = (int(line.split()[1]))
    file.close()
    if name in dic:
        pass
    else:
        dic[name] = 0


def ratings():
    print("Your rating: {}".format(dic[name]))


def default_game():
    print("Okay, let's start")
    while True:
        a = random.choice(["rock", "scissors", "paper"])
        b = input("")
        if b == "!exit":
            print("Bye!")
            break
        elif (a == "rock" and b == "scissors") or (a == "scissors" and b == "paper") or (a == "paper" and b == "rock"):
            print("Sorry, but computer chose {}".format(a))
        elif (b == "rock" and a == "scissors") or (b == "scissors" and a == "paper") or (b == "paper" and a == "rock"):
            print("Well done. Computer chose {} and failed".format(a))
            dic[name] += 100
        elif (b == "rock" and a == "rock") or (b == "scissors" and a == "scissors") or (b == "paper" and a == "paper"):
            print("There is a draw ({})".format(a))
            dic[name] += 50
        elif b == "!rating":
            ratings()
        else:
            print("Invalid input")


def new_game():
    lst = user

    while True:
        c_choice = random.choice(lst)
        user_choice = input("")
        if user_choice == "!exit":
            print("Bye!")
            break
        elif user_choice == "!rating":
            ratings()
        elif user_choice not in lst:
            print("Invalid input")
        else:
            user_index = lst.index(user_choice)
            lst_len = int(math.ceil(len(lst) / 2.0))
            rotate = lst_len - user_index
            lst = (lst[-rotate:] + lst[:-rotate])
            user_newid = lst.index(user_choice)
            win_lst = lst[:user_newid]
            los_lst = lst[user_newid + 1:]

            if user_choice == c_choice:
                print("There is a draw ({})".format(c_choice))
                dic[name] += 50
            elif c_choice in los_lst:
                print("Sorry, but computer chose {}".format(c_choice))
            elif c_choice in win_lst:
                print("Well done. Computer chose {} and failed".format(c_choice))
                dic[name] += 100



name = str(input("Enter your name:"))
print("Hello, {}".format(name))

file_reading()

while True:
    global user
    user = [ x for x in input("").split(",")]
    if "!exit" in user:
        print("Bye!")
        break
    elif len(user) == 1:
        default_game()
        break
    elif "!rating" in user:
        ratings()
    else:
        new_game()
        break
