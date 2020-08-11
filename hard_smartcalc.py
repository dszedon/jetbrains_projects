"""
SMART CALCULATOR

About
Calculators are a very helpful tool that we all use on a regular basis. 
Why not create one yourself, and make it really special? 
In this project, you will write a calculator that not only adds, subtracts, and multiplies, but is also smart enough to remember your previous calculations.

Learning outcomes
Apart from writing a useful program (everyone uses calculators!), you will learn a lot about lists, strings and dictionaries. 
You will also get closer experience with 2 important data structures: the stack and the queue.

Stage 1
Your calculator is taking its first steps: teach it to calculate the sum of two integers and display the result on the screen.

Stage 2
Enable your calculator to keep adding numbers in a loop until the user enters “exit”.

Stage 3
Using lists and strings, make it possible to calculate sums of multiple integers.

Stage 4
Where there is a plus, there is a minus. Using your knowledge of lists and strings, enable the calculator to deal with subtraction as well as addition.

Stage 5
There’s no math without errors: teach your program to alert the user to errors in the case of invalid input.

Stage 6
Working with dict, enable the calculator to use variables.

Stage 7
Time to upgrade and add even more possible operations: multiplication, division, powers, and calculations in parentheses.

"""

def start():

    while True:

        numbers = [x for x in input().split()]

        try:

            # CHECK FOR COMMANDS
            if check_command(numbers) == "ERROR":
                raise Exception

            # CHECK FOR VARIABLE IN MEMORY
            elif len(numbers) == 1 and numbers[0].isalpha():
                one_in_memory(numbers)
                raise Exception

            # CHECK FOR MOST ERRORS
            if error_checks(numbers) == "ERROR":
                raise Exception

        except Exception:
            pass

        else:
            try:
                # CHECK FOR MEMORY SAVES
                for x in numbers:
                    if "=" in x:
                        memory_save(numbers)
                        raise Exception

                if check_parentesis(numbers) == "ERROR":
                    raise Exception

                numbers = check_operators(numbers)
                if numbers == "ERROR":
                    raise Exception

            except Exception:
                pass

            else:
                numbers = memory_check(numbers)

                print(rpn_calculator(rpn_converter(numbers)))
        finally:
            clean()


def error_checks(numbers):

    # a2a
    if len(numbers) == 1:
        if numbers[0].isalpha == False and numbers[0].isdigit() == False:
            print("Unknown variable")
            return "ERROR"

    # NOT IN MEMORY, b = c
    elif len(numbers) == 3:

        if numbers[0].isalpha() == False and numbers[0].isdigit() == False:
            print("Invalid variable")
            return "ERROR"

        elif numbers[2].isalpha() and numbers[2] not in memory:
            print("Unknown variable")
            return "ERROR"

    if numbers.count("=") > 1:
        print("Invalid expression")
        return "ERROR"


def clean():
    del stack[:]
    postfix = ""


def check_command(numbers):

    commands = ["/exit", "/help"]

    if numbers[-1].startswith("/"):
        if numbers[-1] in commands:
            if "/exit" in numbers:
                print("Bye!")
                quit()
            elif "/help" in numbers:
                print("The program calculates the sum of numbers")
                return "ERROR"
        else:
            print("Unknown command")
            return "ERROR"


def one_in_memory(numbers):
    if numbers[0] in memory:
        print(memory[numbers[0]])
    else:
        print("Unknown variable")


def check_parentesis(numbers):

    parentesis_count = ""

    # Check for parentesis
    for x in numbers:
        if "(" in x or ")" in x:
            if "(" in x:
                parentesis_count = parentesis_count + str(x[0])

            elif ")" in x:
                parentesis_count = parentesis_count + str(x[1])

    if parentesis_count.count("(") != parentesis_count.count(")"):
        print("Invalid expression")
        return "ERROR"


def memory_save(numbers):

    # [B, =, A]
    if (len(numbers) == 3) and (numbers[2] in memory):
        memory[numbers[0]] = memory[numbers[2]]

    elif (len(numbers) == 3) and (numbers[0] in memory):
        memory[numbers[0]] = numbers[2]

    # [A, =, 3]
    elif (len(numbers) == 3) and (numbers[0] not in memory):
        memory[numbers[0]] = numbers[2]

    # [A=, 2] or [A,=2]
    elif len(numbers) == 2:
        #  [A=, 2]
        if "=" in numbers[0]:
            new_item, erase_item = numbers[0].split("=")
            numbers[0] = new_item
        # [A, =2]
        if "=" in numbers[1]:
            erase_item, new_item = numbers[1].split("=")
            numbers[1] = new_item
        memory[numbers[0]] = numbers[1]


def check_operators(numbers):

    new_numbers = []

    # Check for operators length and correct them
    for x in numbers:
        if "+" in x:
            new_numbers.append("+")

        elif "-" in x:
            if x[-1].isdigit():
                new_numbers.append(x)
            elif len(x) % 2 == 1:
                new_numbers.append("-")
            else:
                new_numbers.append("+")

        elif (x.count("/") > 1) or (x.count("*") > 1):
            print("Invalid expression")
            return "ERROR"

        else:
            new_numbers.append(x)

    return new_numbers


def memory_check(numbers):

    new_numbers = []

    for x in numbers:
        if x in memory:
            new_numbers.append(memory[x])
        else:
            new_numbers.append(x)

    return new_numbers


# FUNCTIONS FOR RPN CONVERTER AND CALCULATOR
def rpn_converter(string):
    global postfix

    for x in string:

        if "-" in x and len(x) > 1:
            postfix = postfix + " " + x

        elif x.isdigit():
            postfix = postfix + " " + x

        elif x in operators:
            if len(stack) == 0:
                stack.append(x)
            else:
                compare_operators(x)

        elif ("(" in x) or (")" in x):
            parentesis_divider(x)

    while len(stack) >= 1:
        postfix = postfix + " " + stack.pop()

    return postfix


def compare_operators(operator2):
    global postfix

    operator1 = stack[-1]

    if (operator1 == "(") or (operators[operator2] > operators[operator1]):
        stack.append(operator2)

    else:
        postfix = postfix + " " + stack.pop()
        while operators[operator2] < operators[operator1]:
            if operator1 == "(":
                stack.pop()
                break
            if len(stack) == 0:
                stack.append(operator2)
                break
            postfix = postfix + " " + stack.pop()
        else:
            stack.append(operator2)


def parentesis_divider(string):
    global postfix

    if "(" in string:
        for x in string:
            if x == "(":
                stack.append(x)
            elif x.isdigit():
                postfix = postfix + " " + x
    else:
        for x in string:
            if x == ")":
                while stack[-1] != "(":
                    postfix = postfix + " " + stack.pop()
                    if stack[-1] == "(":
                        stack.pop()
                        break
            elif x.isdigit():
                postfix = postfix + " " + x


def rpn_calculator(formula):
    formula = formula.split()

    for x in formula:
        if x.isdigit() or ("-" in x and len(x) > 1):
            stack.append(x)
        elif x in operators:
            operations(x)

    return stack.pop()


def operations(operator):

    val2 = int(stack.pop())
    val1 = int(stack.pop())

    if operator == "+":
        stack.append(val1 + val2)
    elif operator == "-":
        stack.append(val1 - val2)
    elif operator == "*":
        stack.append(val1 * val2)
    elif operator == "/":
        stack.append(val1 / val2)
    elif operator == "^":
        stack.append(val1 ** val2)


operators = {"-": 1, "+": 1, "*": 2, "/": 3, "^": 4}
parentesis = ["(", ")"]
memory = {}
stack = []
postfix = ""
result = 0

start()
