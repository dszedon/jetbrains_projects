"""
HANGMAN GAME

About
Games can help you kill time when you’re bored. But before smartphones, people played games the classic way – with paper and pencil. 
Let’s recreate one such game and improve your programming skills in the process. 
In this project, you will code Hangman, a game where the player has to guess a word, letter by letter, in a limited number of attempts. 
Make a program that plays Hangman with you – and good luck with the guessing!

Learning outcomes
Best project for Python Basics: uses functions, loops, lists, and other variables. 
The Random module is a cherry on top. 
Don’t be intimidated by the number of stages – they ensure that your immersion in Python is smooth and safe.

Stage 1
Welcome the user: print “The game will be available soon”.

Stage 2
For starters, let’s give the player only one chance to guess the word. 
Learn and use “Input” and “if” to implement this stage.

Stage 3
Let’s make the game more challenging: now it will randomly choose one of four words from a list.

Stage 4
Enable hints in your game: let it show the total length of the word or its first three letters. 
Slicing will help you implement this part.

Stage 5
Use a loop to extend the number of attempts to eight. Now we’re talking!

Stage 6
The outcome of the game may be fatal, which makes the game all the more exciting. 
Implement this feature so that players don’t lose strikes when they guess a letter right. 
The While loop will help.

Stage 7
Improve the game by handling different error cases. 
Repeating a letter, entering too many characters, or using non-Latin characters shouldn’t cost your player a strike.

Stage 8
While a dinner starts with the menu, our project ends with one. 
Create a menu for your game so that players can replay it or exit.

"""

import random

tries = 8
lst = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(lst)
dashes = str('-' * (len(word)))
new_dashes = dashes
guesses = []
winner = 0
while True:
    
    user = input('Type "play" to play the game, "exit" to quit:')
    
    if user == "play":
        
        print("H A N G M A N")
        while(tries > 0):
            print()
            print(new_dashes)
            in_letter = input("Input a letter:")
            
            if (len(in_letter) > 1) or (in_letter == None):
                print("You should input a single letter")
                tries += 1
            elif in_letter in guesses:
                print("You already typed this letter")
                tries += 1
            elif in_letter.islower() == False:
                print("It is not an ASCII lowercase letter")
                tries += 1
            elif in_letter in word:
                letter_index = word.find(in_letter)
                new_dashes = new_dashes[:letter_index] + in_letter + new_dashes[letter_index + 1:]
                winner += 1
                tries += 1
            elif in_letter not in word:
                print("No such letter in the word")
            guesses.append(in_letter)
            tries -= 1

        if winner == len(word):
            print("You guessed the word!")
            print("You survived!")
        else:
            print("You are hanged!")

    elif user == "exit":
        break
    
    
