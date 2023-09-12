num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
which = input("What Operation: ")

if(which == "plus" or which == "add"):
    answer = num1 + num2
elif(which == "minus" or which == "subtract"):
    answer = num1 - num2
elif(which == "times" or which == "mulitply"):
    answer = num1 * num2
elif(which == "divide"):
    answer = num1 / num2

print(f"{num1} {which} {num2} equals {answer}")


    