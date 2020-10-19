"""
Multilingual Online Translator
"""
import requests, argparse
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0"
session = requests.Session()

parser = argparse.ArgumentParser()
parser.add_argument("src", type=str)
parser.add_argument("out", type=str)
parser.add_argument("word", type=str)
args = parser.parse_args()


def translate():

    languages = {
        "1": "arabic",
        "2": "german",
        "3": "english",
        "4": "spanish",
        "5": "french",
        "6": "hebrew",
        "7": "japanese",
        "8": "dutch",
        "9": "polish",
        "10": "portuguese",
        "11": "romanian",
        "12": "russian",
        "13": "turkish",
    }

    if args.out == "all":
        pass
    else:
        support_lang = [languages[x] for x in languages]
        if args.out not in support_lang:
            print(f"Sorry, the program doesn't support {args.out}")
            exit()

    src_lang = args.src
    input_word = args.word

    if args.out == "all":
        for x in languages:
            if languages[x] == args.src:
                pass
            else:
                out_lang = languages[x]
                printing(src_lang, out_lang, input_word, 1)
    else:
        out_lang = args.out
        printing(src_lang, out_lang, input_word, 5)


def printing(src_lang, out_lang, input_word, n):

    lst_word, lst_examples_out, lst_examples_src = get_translation(
        src_lang, out_lang, input_word
    )

    print(f"\n{out_lang.capitalize()} Translations:")
    write_file(input_word, f"\n{out_lang.capitalize()} Translations:")
    for x in range(n):
        print(lst_word[x])
        write_file(input_word, lst_word[x])

    print(f"\n{out_lang.capitalize()} Examples:")
    write_file(input_word, f"\n{out_lang.capitalize()} Examples:")
    for x in range(n):
        print(lst_examples_src[x])
        write_file(input_word, lst_examples_src[x])
        print(lst_examples_out[x])
        write_file(input_word, lst_examples_out[x])
        print()


def get_translation(src_lang, out_lang, input_word):

    words = {"class": "translation"}
    examples_src = {"class": "src ltr"}

    if out_lang == "arabic":
        examples_out = {"class": "trg rtl arabic"}
    elif out_lang == "hebrew":
        examples_out = {"class": "trg rtl"}
    else:
        examples_out = {"class": "trg ltr"}

    url = f"https://context.reverso.net/translation/{src_lang}-{out_lang}/{input_word}"
    response = session.get(url, headers={"User-Agent": user_agent})

    if response.status_code == 404:
        print(f"Sorry, unable to find {input_word}")
        exit()
    elif response.status_code != 200:
        print("Something wrong with your internet connection")
        exit()
    else:
        soup = BeautifulSoup(response.content, "html.parser")

        translate_word = soup.find_all("a", words)
        examples_src = soup.find_all("div", examples_src)
        examples_out = soup.find_all("div", examples_out)

        translate_lst = [" ".join(x.text.split()) for x in translate_word]
        translate_lst.pop(0)  # elimitate the word 'Translation'

        src_example_lst = [" ".join(x.text.split()) for x in examples_src]
        out_example_lst = [" ".join(x.text.split()) for x in examples_out]

        return translate_lst, out_example_lst, src_example_lst


def write_file(input_word, *text):
    path = f"{input_word}.txt"
    with open(path, "a") as file:
        file.write(" ".join(text) + "\n")


translate()


