"""
REGEX ENGINE

About
Regular expressions are a fundamental part of computer science and natural language processing. 
In this project, you will write an extendable regex engine that can handle basic regex syntax, 
including literals (a, b, c, etc.), wild-cards (.), 
and metacharacters (?, *, +, ^, $).

"""
def comparing(regex, string):

    if regex == ".":
        regex = string

    if not regex:
        return True
    elif not string:
        return True if not regex else False
    else:
        return True if regex == string else False


def matching(regex, string):
    metachar_lst = ["?", "*", "+"]

    if regex:
        if string:
            if regex[0] != "\\" and len(regex) > 1 and regex[1] in metachar_lst:
                return stage_5(regex, string)
            else:
                if regex[0] == "\\":
                    regex = regex[1:]

                if comparing(regex[0], string[0]):
                    regex = regex[1:]
                    string = string[1:]
                    return matching(regex, string)
                else:
                    return False
        else:
            if regex[0] == "$":
                return True
            else:
                return False
    else:
        return True


def stage_3(regex, string):

    if comparing(regex, string):
        return True
    else:
        if not string:
            return False
        else:
            if matching(regex, string):
                return True
            else:
                string = string[1:]
                return stage_3(regex, string)


def stage_4(regex, string):

    if "^" in regex:
        regex = regex[1:]
        return matching(regex, string)
    elif "$" in regex:
        return stage_3(regex, string)
    else:
        return stage_3(regex, string)


def stage_5(regex, string):

    if regex[1] == "?":
        return what(regex, string)
    elif regex[1] == "*":
        return mult(regex, string)
    elif regex[1] == "+":
        return plus(regex, string)


def what(regex, string):

    if comparing(regex[0], string[0]):
        regex = regex[2:]
        string = string[1:]
        return matching(regex, string)
    else:
        regex = regex[2:]
        return matching(regex, string)


def mult(regex, string):

    if comparing(regex[0], string[0]):
        if len(string) == 1:
            regex = regex[2:]
            return matching(regex, string)
        else:
            string = string[1:]
            return matching(regex, string)
    else:
        regex = regex[2:]
        return matching(regex, string)


def plus(regex, string):
    if comparing(regex[0], string[0]):
        if len(string) == 1:
            regex = regex[2:]
            return matching(regex, string)
        else:
            if comparing(string[0], string[1]):
                string = string[1:]
                return matching(regex, string)
            else:
                regex = regex[2:]
                string = string[1:]
                return matching(regex, string)
    else:
        return False
    

# for testing
# x = "colou\\?r|colour"
# user_regex, user_string = x.split("|")

user_regx, user_inpt = input().split("|")
print(stage_4(user_regx,user_inpt))

