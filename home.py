"""
This program takes user information and outputs the optimal area to buy a home
If user puts in value of budget less that 1000000...
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
        print("The optimal city for you to shop is Aspen/Vail")
    elif 999 > price6 > 500:
        print("The optimal city for you to shop is Denver")
    else:
        print("The optimal are for you to shop is Lakewood")
if homestate == " Connecticut" or homestate == " connecticut":
    greeting()
    price7 = price()
    if price7 > 1000000:
        print("The optimal city for you to shop is Greenwich")
    elif 999 > price7 > 500:
        print("The optimal city for you to shop is Ridgefield")
    else:
        print("The optimal are for you to shop is Trumbull")    
if homestate == " Delaware" or homestate == " delaware":
    greeting()
    price8 = price()
    if price8 > 1000000:
        print("The optimal city for you to shop is Bethany Beach")
    elif 999 > price8 > 500:
        print("The optimal city for you to shop is Rehoboth Beach")
    else:
        print("The optimal are for you to shop is Lewes")
if homestate == " Florida" or  homestate == " florida":
    greeting()
    price9 = price()
    if price9 > 1000000:
        print("The optimal city for you to shop is Boca Raton/Palm Beach")
    elif 999 > price9 > 500:
        print("The optimal city for you to shop is Highland Beach")
    else:
        print("The optimal are for you to shop is Sunny Isles")
if homestate == " Georgia" or homestate == " georgia":
    greeting()
    price9 = price()
    if price9 > 1000000:
        print("The optimal city for you to shop is Milton")
    elif 999 > price9 > 500:
        print("The optimal city for you to shop is Atlana")
    else:
        print("The optimal are for you to shop is Greensboro")
