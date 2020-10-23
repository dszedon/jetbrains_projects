"""
Hangman

About
Hangman is a popular yet grim puzzle game. 
A cruel computer hides a word from you, which you try to guess letter by letter. 
If you fail, you'll be “hanged”. 
If you win, you'll survive. 
You’ve probably played the game at least once or twice. 
Now you can actually create this game yourself!

"""

import random

class Hangman:
    
    def __init__(self):
        self.lst = ('python', 'java', 'kotlin', 'javascript')
        self.word = random.choice(self.lst)
        self.dicc = {lttr: indx for (indx, lttr) in enumerate(self.word)}
        self.tries = 0
        self.dashes = str('-' * (len(self.word)))
        self.new_dashes = self.dashes
        self.guesses = []
        self.winner = 0
    
    
    def start(self):
        print("H A N G M A N")
        while True:
            self.action = input('Type "play" to play the game, "exit" to quit: ')
            if self.action == "play":
                self.play()
            else:
                break
    
    
    def play(self):
        while True:
            print("\n" + self.new_dashes)
            
            self.in_letter = input("Input a letter: ")
            
            if (len(self.in_letter) > 1) or (self.in_letter == None):
                print("You should input a single letter")
            elif self.in_letter.islower() == False:
                print("It is not an ASCII lowercase letter")
            elif self.in_letter in self.dicc:
                self.letter_index = self.dicc[self.in_letter]
                self.new_dashes = self.new_dashes[:self.letter_index] + self.in_letter + self.new_dashes[self.letter_index + 1:]
                self.dicc.pop(self.in_letter)
                self.winner += 1
            elif self.in_letter in self.guesses:
                print("You already typed this letter")
            elif self.in_letter not in self.dicc:
                print("No such letter in the word")
                self.tries += 1

            self.guesses.append(self.in_letter)
            if self.tries == 8:
                print("You lost! \n")
                break
            elif self.winner == len(self.word):
                print("You guessed the word!")
                print("You survived!")
                break

game = Hangman()
game.start()
