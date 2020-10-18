"""
Multilingual Online Translator
"""
import requests
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0"
session = requests.Session()


def testing_lang(languages):
    src_lang = "3"  # english
    out_lang = "0"  # spanish
    input_word = "hello"
    return src_lang, out_lang, input_word


def translate():
    languages = {
        "1": "Arabic",
        "2": "German",
        "3": "English",
        "4": "Spanish",
        "5": "French",
        "6": "Hebrew",
        "7": "Japanese",
        "8": "Dutch",
        "9": "Polish",
        "10": "Portuguese",
        "11": "Romanian",
        "12": "Russian",
        "13": "Turkish",
    }

    print("Hello, you're welcome to the translator. Translator supports:")

    for x, y in enumerate(languages, start=1):
        print(x, languages[y])

    src_lang = input('Type the number of your language:\n')
    out_lang = input('Type the number of language you want to translate to:\n')
    input_word = input('Type the word you want to translate:\n')

    # src_lang, out_lang, input_word = testing_lang(languages)

    if out_lang == "0":
        for x in languages:
            if x == src_lang:
                pass
            else:
                src_lan = languages[src_lang]
                out_lang = languages[x]
                printing(src_lan, out_lang, input_word, 1)
    else:
        src_lang = languages[src_lang]
        out_lang = languages[out_lang]
        printing(src_lang, out_lang, input_word, 5)


def printing(src_lang, out_lang, input_word, n):

    src_lang = src_lang.lower()
    out_lang = out_lang.lower()

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
    #  examples = {"class": "example"}
    examples_src = {"class": "src ltr"}

    if out_lang == "arabic":
        examples_out = {"class": "trg rtl arabic"}
    elif out_lang == "hebrew":
        examples_out = {"class": "trg rtl"}
    else:
        examples_out = {"class": "trg ltr"}

    url = f"https://context.reverso.net/translation/{src_lang}-{out_lang}/{input_word}"

    response = session.get(url, headers={"User-Agent": user_agent})

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

