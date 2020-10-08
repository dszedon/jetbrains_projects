"""
Flash Cards

About
When learning a new language, it can be hard to remember all the new vocabulary, which is exactly where flashcards can help. 
Typically, flashcards show a hint (a task or a picture) on one side and the right answer on the other. 
Flashcards can be used to remember any sort of data, so if you want to create a useful tool to help your learning and your programming skills, 
this project is for you.

"""

from io import StringIO


memory_file = StringIO()


def start():
    flash_cards = {}
    cards_mistakes = {}

    while True:
        user_action = memory_print(
            "Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n",
            1,
        )

        if user_action == "add":
            flash_cards = add_card(flash_cards)
        elif user_action == "remove":
            flash_cards = remove(flash_cards)
        elif user_action == "import" or user_action == "export":
            flash_cards = export_import(user_action, flash_cards)
        elif user_action == "ask":
            cards_mistakes = ask(flash_cards, cards_mistakes)
        elif user_action == "exit":
            memory_print("Bye bye!\n", 0)
            quit()
        elif user_action == "log":
            logger()
            memory_file = StringIO()
        elif user_action == "hardest card":
            memory_print(hardest_card(cards_mistakes), 0)
        elif user_action == "reset stats":
            cards_mistakes = reset(cards_mistakes)


def memory_print(string, val):

    if val == 0:
        memory_file.read()
        memory_file.write(string)
        print(string)
    elif val > 0:
        memory_file.read()
        memory_file.write(string)
        user_input = input(string)
        memory_file.read()
        memory_file.write(user_input)
        return user_input


def add_card(flash_cards):

    while True:
        try:
            card = str(memory_print("The card:\n", 1))
            if card in flash_cards:
                raise Exception
        except Exception:
            memory_print('The card "{}" already exists.'.format(card), 0)
        else:
            while True:
                try:
                    definition = str(memory_print("The definition of the card:\n", 1))
                    if definition in flash_cards.values():
                        raise Exception
                except Exception:
                    memory_print(
                        'The definition "{}" already exists.'.format(definition), 0
                    )
                else:
                    flash_cards[card] = definition
                    memory_print(
                        'The pair ("{}":"{}") has been added.'.format(card, definition),
                        0,
                    )
                    return flash_cards


def remove(flash_cards):
    try:

        card = memory_print("Which card:\n", 1)
        if card not in flash_cards:
            raise Exception
    except Exception:
        memory_print("""Can't remove "{}": there is no such card.""".format(card), 0)
        return flash_cards
    else:
        flash_cards.pop(card)
        memory_print("The card has been removed.", 0)
        return flash_cards


def export_import(action, flash_cards):

    file_name = str(memory_print("File name:\n", 1))
    user_path = "{}".format(file_name)

    if action == "import":
        flash_cards = import_cards(user_path, flash_cards)
        return flash_cards
    else:
        export_cards(user_path, flash_cards)
        return flash_cards


def import_cards(user_path, flash_cards):
    line_count = 0
    if flash_cards is None:
        flash_cards = {}

    try:
        with open(user_path, "r", encoding="utf-8") as user_file:
            for line in user_file:
                elements = line.split("\n")
                elements = elements[0].split(":")
                card, definition = elements[0], elements[1]
                flash_cards[card] = definition
                line_count += 1

        memory_print("{} cards have been loaded.".format(line_count), 0)
        return flash_cards

    except FileNotFoundError:
        memory_print("File not found.", 0)


def export_cards(user_path, flash_cards):
    count_cards = 0
    with open(user_path, "w", encoding="utf-8") as user_file:
        for keys, values in zip(flash_cards.keys(), flash_cards.values()):
            user_file.write("{}:{}\n".format(keys, values))
            count_cards += 1

    memory_print("{} cards have been saved.".format(count_cards), 0)


def ask(flash_cards, cards_mistakes):
    questions_number = 0

    ask_number = int(memory_print("How many times to ask?\n", 1))
    while True:
        for card in flash_cards:
            cards_mistakes = get_def(flash_cards, cards_mistakes, card)
            questions_number += 1
            ask_number -= 1

            if ask_number == 0:
                return cards_mistakes


def get_def(flash_cards, cards_mistakes, card):

    try:
        if cards_mistakes[card] > 0:
            pass
    except:
        cards_mistakes[card] = 0

    answer = str(memory_print('Print the definition of "{}":\n'.format(card), 1))

    if answer in flash_cards.values():
        if answer == flash_cards[card]:
            memory_print("Correct!\n", 0)
            return cards_mistakes

        else:
            key = get_key(flash_cards, answer)
            memory_print(
                'Wrong. The right answer is "{}", but your definition is correct for "{}".\n'.format(
                    flash_cards[card], key
                ),
                0,
            )
            cards_mistakes[card] += 1
            return cards_mistakes
    else:
        memory_print('Wrong. The right answer is "{}".\n'.format(flash_cards[card]), 0)
        cards_mistakes[card] += 1
        return cards_mistakes


def get_key(flash_cards, definition):
    for key, value in flash_cards.items():
        if definition == value:
            return key


def logger():
    file_name = memory_print("File name:\n", 1)

    with open(file_name, "w") as log:
        for line in memory_file:
            log.write(line)

    memory_print("The log has been saved.\n", 0)


def hardest_card(cards_mistakes):
    if cards_mistakes:
        return get_errors(cards_mistakes)
    else:
        return "There are no cards with errors.\n"


def get_errors(cards_mistakes):
    val = 0
    lst = []

    for x in cards_mistakes:
        if cards_mistakes[x] >= val:
            if cards_mistakes[x] == 0:
                pass
            else:
                lst.append(x)
                val = cards_mistakes[x]

    if not lst:
        return "There are no cards with errors.\n"
    elif len(lst) > 1:
        sep = ", "
        hard_card = sep.join(lst)
        return 'The hardest cards are "{}". You have "{}" errors answering them.\n'.format(hard_card, val)
    else:
        hard_card = lst[0]
        return 'The hardest card is "{}". You have "{}" errors answering it.\n'.format(hard_card, val)




def reset(cards_mistakes):
    for x in cards_mistakes:
        cards_mistakes[x] = 0
    memory_print("Card statistics have been reset.\n", 0)
    return cards_mistakes


start()
