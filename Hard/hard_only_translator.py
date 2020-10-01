"""
Multilingual Online Translator
"""

import requests
from bs4 import BeautifulSoup


def translate():

    output_lang = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:\n')
    output_word = input('Type the word you want to translate:\n')
    # output_word = "hello"
    print('You chose "{}" as the language to translate "{}" to.'.format(output_lang, output_word))

    lst_word = get_words(output_word)
    lst_examples = get_examples(output_word)

    print("Context examples:\n")

    print("French Translations:")
    for x in range(5):
        print(*lst_word[x])

    print("\nFrench Examples:")
    for x in range(5):
        print(*lst_examples[x])


def get_words(output_word):

    user_agent = 'Mozilla/5.0'
    words = {"class": "translation ltr dict no-pos"}
    url = 'https://context.reverso.net/translation/english-french/{}'.format(output_word)

    response = requests.get(url, headers={'User-Agent': user_agent})
    print(response.status_code, "OK\n")

    soup = BeautifulSoup(response.content, "html.parser")
    translate_word = soup.find_all("a", words)

    translate_lst = [x.text.split() for x in translate_word]

    return translate_lst


def get_examples(output_word):

    user_agent = 'Mozilla/5.0'
    examples = {"class": "trg ltr"}
    url = 'https://context.reverso.net/translation/english-french/{}'.format(output_word)

    response = requests.get(url, headers={'User-Agent': user_agent})

    soup = BeautifulSoup(response.content, "html.parser")
    translate_examples = soup.find_all("div", examples)

    example_lst = [x.text.split() for x in translate_examples]

    return example_lst


translate()
