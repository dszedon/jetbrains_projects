"""
Description:

Finally, let's add to our calculator the capacity to compute the differentiated payment. 
In such a kind of payment where the part for reducing the credit principal is constant. 
Another part of the payment is for interest repayment and it reduces during the credit term. 
It means that the payment is different each month. Let’s look at the formula:

Objectives:

At this stage, it is required to implement these features:

the calculation of differentiated payment. 
To do this, the user may run the program specifying interest, count of periods and credit principal.

a capacity to calculate the same values as in the previous stage for annuity payment (principal, count of periods and value of the payment). 
A user specifies all known parameters with command-line arguments, while a single parameter will be unknown. 
This is the value the user wants to calculate.

handling of invalid parameters. 
It's a good idea to show an error message Incorrect parameters in case of invalid parameters (they are discussed in detail below).

"""

import math
import argparse
from sys import argv


def calc_diff(p, n, i):
    i = i / (12 * 1)
    dm2 = 0
    n = int(n)
    for m in range(1, n + 1):
        dm = math.ceil((p / n) + i * (p - ((p * (m - 1)) / n)))
        dm = int(dm)
        print("Month {}: paid out {}".format(m, dm))
        dm2 = dm2 + dm
    op = int(dm2 - p)
    print("Overpayment = {}".format(op))


def calc_annuity(p, n, i):
    i = i / (12 * 1)
    a = math.ceil(p * ((i * (1 + i)**n) / ((1 + i)**n - 1)))
    print("Your annuity payment = {}!".format(int(a)))
    op = int((a * n) - p)
    print("Overpayment = {}".format(op))


def calc_principal(a, n, i):
    i = i / (12 * 1)
    p = math.floor(a / (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1)))
    print("Your credit principal = {}!".format(int(p)))
    op = int((a * n) - p)
    print("Overpayment = {}".format(op))


def calc_time(p, a, i):
    i = i / (12 * 1)
    n = math.ceil(math.log((a / (a - i * p)), 1 + i))
    years = int(math.floor(n / 12))
    months = int(n % 12)
    if years == 0:
        print("You need {} months to repay this credit!".format(months))
    elif months == 0:
        print("{} years".format(years))
    else:
        print("You need {} years to repay this credit!".format(years))
    op = int((a * n) - p)
    print("Overpayment = {}".format(op))


parser = argparse.ArgumentParser()

parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=float)
parser.add_argument("--annuity", type=float)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)
parser.add_argument("--periods", type=float)
args = parser.parse_args()

if len(argv) < 5:
    print("Incorrect parameters")

elif args.type is None:
    print("Incorrect parameters")

elif args.type == "annuity":
    if (args.principal) and (args.payment) and (args.periods):
        print("Incorrect parameters")
    elif (args.periods is None) and (args.annuity is None):
        p = args.principal
        a = args.payment
        i = args.interest / 100
        calc_time(p, a, i)
    elif (args.principal is None) and (args.annuity is None):
        a = args.payment
        n = args.periods
        i = args.interest / 100
        calc_principal(a, n, i)
    elif args.annuity is None:
        p = args.principal
        n = args.periods
        i = args.interest / 100
        calc_annuity(p, n, i)

elif args.type == "diff":
    if (args.payment):
        print("Incorrect parameters")
    elif (args.principal) and (args.periods) and (args.interest):
        p = args.principal
        n = args.periods
        i = args.interest / 100
        calc_diff(p, n, i)
