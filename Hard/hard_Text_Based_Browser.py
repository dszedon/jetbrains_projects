"""

TEXT-BASED BROWSER

About
Sometimes you need to read online documentation or find something on the Internet from the command line or terminal. 
So, let's use Python to create a text-based browser! Of course, making a real, full-blown browser is a very difficult task. 
In this project, you'll create a very simple browser that will ignore JavaScript and CSS, won't have cookies, and will only process a limited set of tags. 
Still, it will be useful and, most importantly, fun to program!

Learning outcomes
You will learn how HTTP works and how to handle its protocols using Python. 
You will also learn all about Python input/output, as well as parsing HTML.

Stage 1
Let's create the first capability for our browser! 
It has to read the URL and show the user a "hard-coded" website with some news.

Stage 2
Time to add some user-friendliness. 
The program should store our pages as files and show them if the user enters a shortened request. 
Watch for inappropriate input, though! 

Stage 3
Sometimes you want to revisit the past. 
Let's add a “back” button by using the stack. 

Stage 4
Time to play in a new way. 
Now only real web pages! Get to know the Request library. 

Stage 5
Let’s enhance the readability of our pages and teach our browser to output only a certain text from HTML tags. 

Stage 6
Look-and-feel is important to the browser experience. 
Let's read about a new library, experiment a bit, and highlight our links in blue. 

"""

import os
import argparse
import requests
from collections import deque
from colorama import Fore, Style
from bs4 import BeautifulSoup


def new_folder(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def run():

    while True:
        user = str(input())

        user = check_webpage(user)

        if user == "pass":
            pass
        elif user == "error":
            print("Error: Incorrect URL")
        else:
            user = url_content(user)
            tab_lst.append(user)


def check_webpage(string):

    if string in tab_lst:
        read_file(string)
        return "pass"
    elif string == "back":
        read_file(tab_lst.popleft())
        return "pass"
    elif string.count(".") >= 1:
        return string
    elif string == "exit":
        exit()
    else:
        return "error"


def url_content(url):
    r = requests.get("https://{}".format(url))
    soup = BeautifulSoup(r.content, "html.parser")
    content = soup.find_all(tags)

    if url.endswith(".org"):
        url = url.replace(".org", "")
    elif url.endswith(".com"):
        url = url.replace(".com", "")

    for lines in content:
        if lines.a:
            print(Fore.BLUE + str(lines.text) + "\n")
            write_file(url, (str(lines.text) + "\n"))
        else:
            print(Fore.WHITE + str(lines.text) + "\n")
            write_file(url, (str(lines.text) + "\n"))

    return url


def write_file(web_page_file, web_page_txt):

    path = "{}/{}".format(directory_name, web_page_file)
    with open(path, 'a') as file:
        file.write(web_page_txt)


def read_file(web_page_file):

    path = "{}/{}".format(directory_name, web_page_file)
    with open(path, 'r') as file:
        for line in file:
            print(line.strip())


parser = argparse.ArgumentParser()
parser.add_argument("tab_dir", type=str)
args = parser.parse_args()
tab_lst = deque()
tags = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
directory_name = args.tab_dir
new_folder(directory_name)


run()

