"""
REGEX ENGINE

About

Learning Outcomes




"""

from collections import deque
import sys

sys.setrecursionlimit(10000)
regx = deque()
inpt = deque()


def comparing(regx, inpt):

    if regx and inpt:

        for indx, lttr in enumerate(regx):
            if lttr == ".":
                regx[indx] = inpt[indx]

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


def check_strings(lst, lst2):
    str1 = "".join(lst)
    str2 = "".join(lst2)
    return True if str1 in str2 else False


user_regx, user_inpt = "app|apple".split("|")

[regx.append(x) for x in user_regx]
[inpt.append(x) for x in user_inpt]

print(comparing(regx, inpt))
