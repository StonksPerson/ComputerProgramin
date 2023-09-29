My_Name = input("what is your name? ")
z = input("input a number: ")
names = {"jacob", "kyle", "Jacob", "Mike"}
words = ('burr', 'mosqu', 'incogn')

def print_my_name(name):
    print(name)

print_my_name(My_Name)

def trip_planner(start, end, duration, mode = "car"):
    print(f"It looks like your tripe from {start}")
    print(f"You are planning to get to {end}")
    print(f"It should take you about {duration} hours")
    print(f"I see you are taking a {mode}")

trip_planner('Paradigm', 'the Delta Center', 0.5, 'Car')

def print_global(variable):
    print(variable)

print_global(z)

def ask(question):
    print(input(question))

ask("What is your name? ")

def FilterList(name):
    filter(names,name)

FilterList("jacob")

def CreateList():
    print(list([1,2,3,4,5,6]))

CreateList()

def MapList(a, b):
    return a + b

x = map(MapList, words,("ito","ito","ito"))

print(list(x))

def PrintRange(Num1, Num2):
    for i in range(Num1, Num2):
        print(i)

PrintRange(int(input("First Number: ")), int(input("Second Number: ")))

def SortList():
    print(sorted(['s', 'e', 'c', 'o', 'n', 'd']))

SortList()

def printNumber():
    print(int("8576309"))

printNumber()

def printString():
    print(str(104.36))

printString()