"""
This program takes user information and outputs the optimal area to buy a home
If user puts in value of budget less than 1000000...
Do not include the 0's after number (ex -> 900,000 = 900)

Author: Jacob Olshanskiy
Date:4-12-22
"""


def price():
    return eval(input("What is your price range"))


def greeting():
    print("Great! Let me do some research")


print()
print("Hello, I can show you the area of your perfect home")
print()
homestate = input("What state would you like to live in").lower()
realhome1 = True
realhome2 = True
realhome3 = True
while realhome1:
    homestate = input("What state would you like to live in")
    print("Based on your state selection of", homestate, "the optimal cities for you to shop in are:")
