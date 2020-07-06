"""
HANGMAN GAME
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
    
    
