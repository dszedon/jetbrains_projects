"""
About
Here, at the beginning of your programmer’s path, creating a simple console chat bot will do wonders to guide you through the basics of coding. 
During this journey you will also play some word and number games that you are going to implement all on your own. 
Pack up and let’s hit the road, my friend!

Learning outcomes
You’ll get to know the basic syntax of Python and write a simple program using variables, conditions, loops, and functions.

Stage 1
Teach your assistant to introduce itself in the console.

Stage 2
Introduce yourself to the bot.

Stage 3
Use your knowledge of strings and numbers to make the assistant guess your age.

Stage 4
Your assistant is old enough to learn how to count. 
And you are experienced enough to apply a for loop at this stage!

Stage 5
At this point, the assistant will be able to check your knowledge and ask multiple-choice questions. 
Add some functions to your code and make the stage even better.

"""

def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print(""""1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.""")
    print('Completed, have a nice day!')
    a = int(input())
    if a == 4:
        print("Completed, have a nice day!")
    else:
        print("Please, try again.")


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
