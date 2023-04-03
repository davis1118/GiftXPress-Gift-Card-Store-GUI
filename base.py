from appJar import gui #imports the gui library from appJar

""" PRESS FUNCTION
This is the function that determines code executed when each button is pressed

"""
#Davis Le (cleaned up/combined overall implementation of the code and created the GUI)
def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Begin Shopping":
        greet_user("Welcome to GiftXPress, the online store where one can purchase multiple, cheap $10 gift cards!", "n", "What category would you like to browse (Retail, Food?)? ", "Are you ready to browse (y/n)? ")
    elif btn == "FAQ - What do we sell?":
        print("\nWhat do we sell? \nWe currently sell cheap $10 gift cards for a limited variety of Food and Retail-related companies. However, we are continually expanding our presence as an online gift shop platform!")
    elif btn == "Gift Cards List - Food":
        print('\nList of currently supported Food-related gift cards:')
        print(foodlist)  
    elif btn == "Gift Cards List - Retail":
        print('\nList of currently supported Retail-related gift cards:')
        print(retaillist)    
    else:
        print('\nWho are we? \nJust a company who wants to safely and quickly process gift card purchases for/from various companies to the buyer. Our price remains at a static $10 per gift card to make the shopping process easy to use and follow!')

#Matthew Tse (created product function and selection)
import pandas
giftcardsdf=pandas.read_csv("giftcard.csv")
retaillist = list(giftcardsdf.Retail)
foodlist = list(giftcardsdf.Food)
totalprice = 0
cart = ' '

#Brandon Chung (made greeting function and title display)
def greet_user(greeting,sentinel,categoryq,readyq): 
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == sentinel:
        canswer = input(categoryq)
        canswer2 = 'retail'
        canswer3 = 'food'
        ranswer = input(readyq)
    if canswer.lower() == canswer2:
        retail("Welcome to our Giftcards section! Here are your choices:",retaillist,"Which giftcards would you like or enter None? ")
    elif canswer.lower() == canswer3:
        food("Welcome to our Giftcards section!  Here are your choices:",foodlist,"Which giftcards would you like or enter None? ")
    else:
        print('Sorry, that item is unavailable. See you next time!')

#Function ask user to pick Retail
def retail(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    retailspick = input(pickq)
    if retailspick == "None":
        print("See you next time!")
    elif retailspick == "Visa":
        closing("Visa",10,"Enjoy your Visa giftcard!" )
    elif retailspick == "Mastercard":
        closing("Mastercard",10,"Enjoy your Mastercard giftcard!" )
    elif retailspick == "Amazon":
        closing("Amazon",10,"Enjoy your Amazon giftcard!" )
    elif retailspick == "Apple":
        closing("Apple",10,"Enjoy your Apple giftcard!" )
    elif retailspick == "Microsoft":
        closing("Microsoft",10,"Enjoy your Microsoft giftcard!" )
    elif retailspick == "Walmart":
        closing("Walmart",10,"Enjoy your Walmart giftcard!" )
    elif retailspick == "Target":
        closing("Target",10,"Enjoy your Target giftcard!" )
    else:
        print('Sorry, that item is unavailable. Please pick another option.')
        retail(greeting,selection,pickq)

#Function ask user to pick a Food
def food(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    foodpick = input(pickq)
    if foodpick == "None":
        print("See you next time!")
    elif foodpick == "Taco Bell":
        closing("Taco Bell",10,"Enjoy your Taco Bell giftcard!" )
    elif foodpick == "Boiling Pot":
        closing("Boiling Pot",10,"Enjoy your Boiling Pot giftcard!" )
    elif foodpick == "Happy Lemon":
        closing("Happy Lemon",10,"Enjoy your Happy Lemon giftcard!" )
    elif foodpick == "Panda Express":
        closing("Panda Express",10,"Enjoy your Panda Express giftcard!" )
    elif foodpick == "Starbucks":
        closing("Starbucks",10,"Enjoy your Starbucks giftcard!" )
    elif foodpick == "Jamba Juice":
        closing("Jamba Juice",10,"Enjoy your Jamba Juice giftcard!" )
    elif foodpick == "Subway":
        closing("Subway",10,"Enjoy your Subway giftcard!" )
    else:
        print('Sorry, that item is unavailable. Please pick another option.')
        food(greeting,selection,pickq)

#Daniel Nguyen (closing/exit functions, along with adjusted total price function)
#Function to display to the user the total price of items purchased
def closing(pickeditem,price,goodbye):
    print("You have chosen $"+str(price), pickeditem)
    total(pickeditem,price)
    more = input("Would you like to buy another gift card (y/n)?")
    if more == "y":
        greet_user("Sure", "n", "No problem! What type of gift card would you like to buy (Retail, Food)? ", "Ready to choose (y/n)? ")
    else:
        print("Your total price for:"+cart+" gift card purchases is $"+str(totalprice)+".","Have a nice day!")
        
#Function for adding up total price of the shopping cart
def total(pickeditem,price):
    global totalprice
    totalprice= totalprice + price
    global cart 
    cart = cart+pickeditem+","

""" GUI DEFINITION AREA
The code below defines the gui, adding buttons, labels, images, color, etc.

"""

#The name of the actual GUI window and size
app=gui("Main Menu","500x500")

#Adds/modifies the title and background on top of the GUI
app.addLabel("title", "Welcome to GiftXPress's Online $10 Gift Card Shop!")
app.setLabelBg("title", "orange")

#Sets the gif image of the GUI and font size of the title
app.addImage("decor","k.gif")
app.setFont(14)

#Adds interactive buttons to select on the GUI
app.addButton("Begin Shopping", press)
app.addButton("FAQ - What do we sell?", press)
app.addButton("FAQ - Who are we?", press)
app.addButton("Gift Cards List - Food", press)
app.addButton("Gift Cards List - Retail", press)
app.addButton("Exit",press)
app.go() #displays the gui


