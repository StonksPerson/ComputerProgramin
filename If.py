salary = int(input("how many years of you been working here?"))
bonus = 0

if(salary >= 5):
    print(f"Your bonus will be {salary * 0.05}")
else:
    print("you don't quallify for a bonus")

Square_width = int(input("give one side of a square"))
Square_height = int(input("give the other side of that same square"))

if(Square_width == Square_height):
    print("Correct")
else:
    print("Wrong >:(")

num1 = int(input(" give me your number "))
num2 = int(input("give me your other number"))

if (num1 > num2):
    print(f"{num1} is bigger")
elif(num1 < num2):
    print(f"{num2} is bigger")
else: print("They are equal")

age1 = int(input("give the first persons age"))
age2 = int(input("give the second persons age"))
age3 = {int(input("give the last persons age")) }

if age1 > age2 and age1 > age3:
    print("person 1 is the oldest")

elif age2 > age3 and age2 > age1:
    print("person 2 is the oldest")

elif age3 > age1 and age3 > age2:
    print("person 3 is the oldest")

if age1 < age2 and age1 < age3:
    print("person 1 is the youngest")

elif age2 < age1 and age2 < age3:
    print("person 2 is the youngest")

elif age3 < age2 and age3 < age1:
    print("person 3 is the youngest")

classesAttended = int(input("how many classes did you attend"))
classesMissed = int(input("how many classes did you miss"))

if classesMissed / classesAttended > 0.75:
    print("YOU CAN DO IT")
else: print("leave")