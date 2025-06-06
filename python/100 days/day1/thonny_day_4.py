#random module
import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float_0_1 = random.random() *10
print(random_float_0_1)
random_float= random.uniform(10, 100)
print(random_float)

flip_coin = random.randint(1, 2)
if flip_coin == 1:
    print('heads')
else:
    print('tails')
#lists
states = ["delavare", "california"]
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[0])
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# 1 option
print(friends[random.randint(0, len(friends)-1)])
# 2 option
print(friends[random.choice(friends)])
fruits.append("Orange")

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
print(fruits_and_veg)
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]

# my paper scissors:
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_weapon = int(input('Choose your weapon 0 is rock, 1 is paper, 2 is scissors\n'))
weapons = [rock, paper, scissors]
computer_weapon = random.randint(0, 2)
print(f"Your weapon is {weapons[user_weapon]}")
print(f"My weapon is {weapons[computer_weapon]}")

if user_weapon == computer_weapon:
    print("It's a draw!")
elif (user_weapon == 0 and computer_weapon == 2
        or user_weapon == 1 and computer_weapon == 0
        or user_weapon == 2 and computer_weapon == 1):
    print("You win!")
else:
    print("You lose!")

