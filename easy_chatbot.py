"""
Description

At the final stage, you will improve your simple bot so that it can give you a test and check your answers. 
The test should be a multiple-choice quiz about programming. 
Your bot has to repeat the test until you answer correctly and congratulate you upon completion.

Objective

Your bot can ask anything you want, but there are two rules for your output:

the line with the test should end with the question mark character;
an option starts with a digit followed by the dot (1., 2., 3., 4.)
If a user enters an incorrect answer, the bot may print a message:
  Please, try again.
The program should stop on the correct answer and print Congratulations, have a nice day! at the end.

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
