num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
which = input("What Operation? please type one of the following: add, subtract, multiply, divide ")

if which == "add":
    answer = num1 + num2
elif which == "subtract":
    answer = num1 - num2
elif which == "mulitply":
    answer = num1 * num2
elif which == "divide":
    answer = num1 // num2

print(f"{num1} {which} {num2} equals {answer}")