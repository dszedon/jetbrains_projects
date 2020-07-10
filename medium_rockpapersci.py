"""
Description

How about some brand new rules? The original game has a fairly small choice of options.

Extended versions of the game are decreasing the probability of draw, so it could be cool to play them.
Now, your program should be able to accept alternative lists of options, like Rock, Paper, Scissors, Lizard, Spock, or even a list like this:

At this stage, before the start of the game, the user will be able to choose the options that will be used. 
After entering his/her name, the user should provide a list of options separated by a comma. For example,

rock,paper,scissors,lizard,spock

If the user inputs an empty line, your program should start the game with default options: rock. paper and scissors.

After the game options are defined, your program should output Okay, let's start

Whatever list of options the user chooses, your program, obviously, 
should be able to identify which option beats which, that is, the relationships between different options. 
First, every option is equal to itself (causing a draw if both user and computer choose the same option). 
Secondly, every option wins over one half of the other options of the list and gets defeated by another half. 
How to determine which options are stronger or weaker than the option you're currently looking at? 
Well, you can try to do it this way: take the list of options (provided by the user or the default one). 
Find the option for which you want to know its relationships with other options. 
Take all the options that follow this chosen option in the list. 
Add to them the list of options that precede the chosen option. 
Now you have another list of options that doesn't include the "chosen" option and 
has the different order of elements in it (first go the options following the chosen one in the original list, 
after them are the ones that precede it). 
So, in this "new" list, the first half of the options will be defeating the "chosen" option, and the second half will get beaten by it.

For example, the user's list of options is rock,paper,scissors,lizard,spock. You want to know what options are weaker than lizard. 
By looking at the list spock,rock,paper,scissors you realize that spock and rock will be beating the lizard, and paper and scissors will get defeated by it. 
For spock it'll be almost the same, but it'll get beaten by rock and paper, and prevail over scissors and lizard. 
For the version of the game with 15 options, you can look at the picture above to understand the relationships between options.

Of course, this is not the most efficient way to determine which option prevails over which. 
You are welcome to try to develop some other methods of tackling this problem.

Objectives:

Objectives
Your program should:

Output a line Enter your name: . Note that the user should enter his/her name on the same line (not the one following the output!)
Read input specifying the user's name and output a new line Hello, <name>
Read a file named rating.txt and check if there's a record for the user with the same name; 
if yes, use the score specified in the rating.txt for this user as a starting point for calculating the score in the current game. 
If no, start counting user's score from 0.
Read input specifying the list of options that will be used for playing the game (options are separated by comma). 
If the input is an empty line, play with default options.
Output a line Okay, let's start
Play the game by the rules defined on the previous stages:
Read user's input
If the input is !exit, output Bye! and stop the game
If the input is the name of the option, then:
Pick a random option
Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
Lose -> Sorry, but computer chose <option>
Draw -> There is a draw (<option>)
Win -> Well done. Computer chose <option> and failed
For each draw, add 50 points to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
If the input corresponds to anything else, output Invalid input
Play the game again (with the same options that were defined before the start of the game)

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
