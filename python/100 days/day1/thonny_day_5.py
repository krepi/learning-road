# loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
 
 student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_exam_score = sum(student_scores)
sum = 0
for score in student_scores:
    sum += score
print(max(student_scores))
max_score= student_scores[0]
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)
# range function
range(1,101)
sum = 0
for i in range(1,101):
    sum += i
print(sum)
for number in range(1,101):
   
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
#password generator
import random
from itertools import count
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
random_symbol_array =[letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
symbols_sum= nr_symbols + nr_letters+ nr_numbers
password = ""
for i in count():
    current_array = random.choice(random_symbol_array)
    if current_array == letters and nr_letters> 0:
        password += random.choice(letters)
        nr_letters -= 1
    elif current_array == symbols and nr_symbols> 0:
        password += random.choice(symbols)
        nr_symbols -= 1
    elif current_array == numbers and nr_numbers> 0:
        password += random.choice(numbers)
        nr_numbers -= 1

    if len(password) == symbols_sum:
        break

print(f"Your password is: {password}")
print(len(password))
# Angelaway
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
        