job = True
name = input("What is your name?: ")
if(name == "John"):
    job == False

programming = input(f"Hello {name}, what programming language do you have the most experince in?: ")
years = input(f"{programming}? Thats awesome! How long have you been in this industry?: ")
salary = input(f"{years}? Amazing! How much are you looking to be paid here?: ")
pet = input(f"{salary}? We will see about that. How many pets do you own?: ")
why = input(f"{pet} pets? That is so cool, I have 2 of my own. Why do you want this job?: I am ")
fit = input(f"Do YOU think that you are fit for this job y/n: ")
if(fit == "n"):
    job = False
    fit = "not "
else: fit = ""
portfolio = input(f"So you do {fit}think you are fit for this job. Do you have a portfolio y/n: ")
if(portfolio == "n"):
    job = False
    portfolio = "That's fine. "
else: portfolio = "Amazing! "
hours = int(input(f"{portfolio}How many hours a week do you want to put in?: "))
if(hours > 50):
    hours_ans = "That is some great initiative!"
else: hours_ans = f"Only {hours} hours? Ok. "
want = input(f"{hours_ans} {name}. Do you want this job y/n: ")

if(portfolio == "That's fine. "):
    job = False
    portfolio = ""
else: portfolio = "do not "

if(want == "n"):
    job = False
    want = "do not "
else: want = ""



if(portfolio == "n"):
    job = False
    portfolio = "not "
else: portfolio = ""

print(f"So {name}, if I have it right you progam in {programming}, you also have {years} of experience. In this job you want to make {salary} dollars. you also have {pet} pets. So you want this job")
print(f"because you are {why}, and you feel that you are {fit}fit for this job. You also do {portfolio}have a portfolio, and you want to work {hours} hours a week. You also {want}want this job")
if(job == True):
    print("I think you will enjoy your time working with us!")
else:
    print("I think you should look for other options.")

