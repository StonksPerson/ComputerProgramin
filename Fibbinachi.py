loops = int(input("To how many digits: "))

fib_1 = 1
fib_2 = 0
print("1")

for i in range(loops - 1):

    new_fib_1 = fib_1 + fib_2
    fib_2 = fib_1
    fib_1 = new_fib_1
    print(fib_1)
