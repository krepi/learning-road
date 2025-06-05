#if else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
     print("You can ride the rollercoaster!")
else:
     print("You can't ride the rollercoaster!")

#modulo
number_to_check = int(input("number you want to check"))
if number_to_check % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
#elif
maths_score = int(input("What is your maths score? "))
english_score = int(input("What is your english score? "))

if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
if english_score >= 90:
    print("You're good at english")




print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        print("pay $5")
    elif age <= 18:
        print("pay $7")
    else:
        print("pay $9")
else:
    print("Sorry you have to grow taller before you can ride.")

#multiple conditions
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    bill = 0
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are  $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adults tickets are $12.")
    wants_photo = input("do you want a photo? Type y for'yes' or n for 'no'\n")
    if wants_photo == "y":
        bill += 3
    print(f"Your bill is ${bill}." )

else:
    print("Sorry you have to grow taller before you can ride.")
#my pizza solution
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"Your final bill is: ${bill}." )
# logical operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55 :
        print("everything gonna be ok!")
    else:
        print("Adult tickets are $12.")
        bill = 0

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or not(age >= 45 and age <= 55):
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
    
#game treasure
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction= input("where U wanna go ? l for left, r for right: ")
if direction == "l":
    print("lets continue")
    travel_type = input("Do you wanna swim (s) or wait (w)")
    if travel_type == "w":
        print("after waiting a while a boat arrived and took you on the island")
        door_colour = input("You see a 3 doors blue , red and yellow. Which colour do you choose?")
        if door_colour == "red":
            print("burned by fire. game over")
        elif door_colour == "yellow":
            print("You win")
        elif door_colour == "blue":
            print("Eaten by beasts. You lose")
        else:
            print("You lose")
    else:
        print("game over")
else:
    print("game over")

    