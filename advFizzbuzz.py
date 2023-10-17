n = int(input("To how many digits "))
fizzname = input("fizz: ")
buzzname = input("buzz: ")
fizz = int(input("fizz number = "))
buzz = int(input("buzz number = "))
output = ''


for i in range(n):

    prime = True
    original = output
    for p in range(2, i):
        if (i + 1) % p == 0:
            prime = False
            break
        if i + 1 == 3:
            prime = True
    if prime == True:
        output = output + "prime"
    else:
        if (i + 1) % fizz == 0:
            output = output + buzzname
        if (i + 1) % buzz == 0:
            output = output + fizzname
        if output == original:
            output = output + str(i + 1)

    output = output + ", "

print(output)

    