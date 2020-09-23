"""
REGEX ENGINE

About
Regular expressions are a fundamental part of computer science and natural language processing. 
In this project, you will write an extendable regex engine that can handle basic regex syntax, 
including literals (a, b, c, etc.), wild-cards (.), 
and metacharacters (?, *, +, ^, $).

Learning outcomes
Learn about the regex syntax, 
practice working with parsing and slicing, 
and get more familiar with boolean algebra and recursion.

Stage 1
Implement a program that compares two single character strings (including the wildcard) and determines if there's a match. 

Stage 2
Extend your engine to compare two equal length strings using recursion.

Stage 3
Add the ability to compare a regex to strings that vary in length. 

Stage 4
Extend the engine to handle the operators ^ and $ that control the position of the regex within a string. 

Stage 5
Support the additional operators ?, *, and + that control the repetition of a character within a string. 

Stage 6
Finally, implement the backslash \ as an escape symbol that allows to use metacharacters as literals. 

"""
from collections import deque
import sys

sys.setrecursionlimit(10000)
regx = deque()
inpt = deque()


def comparing(regx, inpt):

    check_special_char = str(check_char(regx, inpt))

    if check_special_char == "True":
        return True
    elif check_special_char == "False":
        return False

    check_wildcard(regx, inpt)

    if regx and inpt:

        if check_strings(regx, inpt):
            return True
        else:
            if regx == inpt:
                return True
            else:
                inpt.popleft()
                return comparing(regx, inpt)
    else:
        if bool(regx) == False:
            return True
        else:
            return False if bool(inpt) == False else True


def check_strings(regx, inpt):
    regx = "".join(regx)
    inpt = "".join(inpt)
    return True if regx in inpt else False


def check_char(regx, inpt):

    if "$" in regx and "^" in regx:
        regx.popleft()
        regx.pop()
        regx = "".join(regx)
        inpt = "".join(inpt)

        if inpt.startswith(regx) and inpt.endswith(regx):
            return True
        else:
            return False

    elif "^" in regx:
        # regx.popleft()
        check_wildcard(regx, inpt)
        regx = "".join(regx)
        inpt = "".join(inpt)

        if inpt.startswith(regx):
            return True
        else:
            return False

    elif "$" in regx:
        #  regx.pop()
        check_wildcard(regx, inpt)
        regx = "".join(regx)
        inpt = "".join(inpt)

        if inpt.endswith(regx):
            return True
        else:
            return False


def check_wildcard(regx, inpt):

    if "$" in regx:
        regx.pop()
        if len(regx) == 1:
            for indx, lttr in enumerate(regx):
                if lttr == ".":
                    regx[indx] = inpt[-1]
    elif "^" in regx:
        regx.popleft()
        if len(regx) == 1:
            for indx, lttr in enumerate(regx):
                if lttr == ".":
                    regx[indx] = inpt[-1]
    else:
        for indx, lttr in enumerate(regx):
            if lttr == ".":
                regx[indx] = inpt[indx]


user_regx, user_inpt = input().split("|")

[regx.append(x) for x in user_regx]
[inpt.append(x) for x in user_inpt]

print(comparing(regx, inpt))

