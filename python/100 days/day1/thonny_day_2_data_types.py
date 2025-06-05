#Subscripting
print("Hello"[-1])
#Integer
print(123_345)
#Float
print(3.14)
#Boolean
print(True)
print(False)
len("12345")
#type checking
print(type("12345"))
print(type(12345) )
print(type(1234.5))
print(type(True))
#math operators
print(123 +222)
print(4 - 2)
print(4 * 2)
print(2 // 2) #integer as value
print(2 ** 3) #power, exponent

#PEMDAS
# ()
# **
# * OR / left first
# + OP - left first
print(3*3 + 3 / 3 - 3)
print(3*(3 + 3) / 3 - 3)
#task tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

per_person_bill= (bill  + bill * (tip/100)) /people
print(f"Each person should pay: ${per_person_bill}")