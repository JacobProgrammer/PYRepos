"""
This program takes user information and outputs the optimal area to buy a home

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
if homestate == " Alabama" or homestate == " alabama":
    greeting()
    price1 = price()
    if price1 > 1000000:
        print("The optimal city for you to shop is Orange Beach")
    elif 999 > price1 > 500:
        print("The optimal city for you to shop is Vesatvia Hills")
    else:
        print("The optimal are for you to shop is Hoover")
if homestate == " Alaska" or homestate == " alaska":
    greeting()
    price2 = price()
    if price2 > 1000000:
        print("The optimal city for you to shop is Juneau")
    elif 999 > price2 > 500:
        print("The optimal city for you to shop is Anchorage")
    else:
        print("The optimal are for you to shop is Fairbanks")
if homestate == " Arizona" or homestate == " arizona":
    greeting()
    price3 = price()
    if price3 > 1000000:
        print("The optimal city for you to shop is Paridise Valley")
    elif 999 > price3 > 500:
        print("The optimal city for you to shop is Scottsdale")
    else:
        print("The optimal are for you to shop is Cave Creek")
if homestate == " Arkansas" or homestate == " arkansas":
    greeting()
    price4 = price()
    if price4 > 1000000:
        print("The optimal city for you to shop is Fayetteville")
    elif 999 > price4 > 500:
        print("The optimal city for you to shop is Bentonville")
    else:
        print("The optimal are for you to shop is Rogers")
if homestate == " California" or homestate == " california":
    greeting()
    price4 = price()
    if price4 > 1000000:
        print("The optimal city for you to shop is Beverly Hills")
    elif 999 > price4 > 500:
        print("The optimal city for you to shop is Los Angeles")
    else:
        print("The optimal are for you to shop is Canoga Park")
if homestate == " Colorado" or homestate ==" colorado":
    greeting()
    price6 = price()
    if price6 > 1000000:
        print("The optimal city for you to shop is ")
    elif 999 > price6 > 500:
        print("The optimal city for you to shop is ")
    else:
        print("The optimal are for you to shop is ")
