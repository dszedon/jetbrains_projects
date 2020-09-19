"""

Simple Chatty Bot 

About
Here, at the beginning of your programmer’s path, creating a simple console chat bot will do wonders to guide you through the basics of coding. 
During this journey you will also play some word and number games that you are going to implement all on your own. 
Pack up and let’s hit the road, my friend!

"""
class bot():
    def __init__(self, bot_name, birth_year):
        print('Hello! My name is ' + bot_name + '.')
        print('I was created in ' + birth_year + '.')


    def remind_name(self, name):
        print('What a great name you have, ' + name + '!')


    def guess_age(self):
        print("""Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.""")
        rem3 = int(input())
        rem5 = int(input())
        rem7 = int(input())
        age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
        print("Your age is " + str(age) + "; that's a good time to start programming!")


    def count(self, num):
        print('Now I will prove to you that I can count to any number you want.')
        curr = 0
        while curr <= num:
            print(curr, '!')
            curr = curr + 1


    def test(self):
        print("Let's test your programming knowledge.")
        while True:
            answer = int(input("""Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program."""))
            if answer == 2:
                print('Completed, have a nice day!')
                break
            else:
                print("Please, try again.")
                

    def end(self):
        print('Congratulations, have a nice day!')

aid = bot('Aid', '2020')
aid.remind_name(input('Please, remind me your name.\n'))
aid.guess_age()
aid.count(int(input()))
aid.test()
aid.end()
