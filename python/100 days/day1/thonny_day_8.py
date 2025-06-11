def greet():
    print("Welcome to the game!")
    print("I am thinking of a letter ...")
    print("Take a guess.")

greet()
def greet_with(name, location):
    print(f"Hello {name}")
    print( f"What is it like in {location}")

greet_with("Przemek", "Olsztyn")

greet_with(name ="Olsztyn",location ="Przemek", )

def greet_with(name, location):
    print(f"Hello {name}")
    print( f"What is it like in {location}")

greet_with("Przemek", "Olsztyn")

greet_with(name ="Olsztyn",location ="Przemek", )

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
def calculate_love_score(name1,name2):
    low_name1 = name1.lower()
    low_name2 = name2.lower()
    true = ["t","r","u","e"]
    love = ["l","o","v","e"]
    true_sum = 0
    love_sum = 0
    for letter in true:
        true_sum += low_name1.count(letter)
        true_sum += low_name2.count(letter)
    for letter in love:
        love_sum += low_name1.count(letter)
        love_sum += low_name2.count(letter)
    total= str(true_sum) + str(love_sum)
    print(int(total))

calculate_love_score( "Angela Yu","Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")