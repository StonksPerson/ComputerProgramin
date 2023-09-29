word = input("Input a word: ")
AnimalList = ['platypus','dog','cow','horse']
FlowerList = ['Jasmine','lotus','rose','sunflower','done']
list1 = [5, 10, 20, 40]
list2 = ['Tomatoes', 'Potatoes', 'Carrots', 'Cucumbers']
vehicles = ['Car','Cycle','bus','Tempo']
numbers = [12,3,56,67,89,90]
numbers2 = [10,5,6,10,15,20,25]
numbers3 = []
list3 = ['mango','bannana','orange']
list4 = []
count = 0
summ = 0
maxx = 0
minn = 0
se = 0

for i in range(len(word)):
    print(word[i])

for i in range(4):
    print(i)

for i in range(len(AnimalList)):
    if(len(AnimalList) > len(FlowerList)):
        print(AnimalList[i])
    else: print(FlowerList[i])

for i in range(len(list1)):
    for e in range(len(list2)):
        print(str(list1[i]) + " " + list2[e])

for i in range(len(vehicles)):

    if(i == 3):
        break
    print(vehicles[i])

for i in range(len(vehicles)):

    if(i == 2):
        continue
    print(vehicles[i])

for i in range(len(numbers)):
    count += 1

print(count)

for i in range(len(numbers2)):
    summ += numbers2[i]

print(summ)

for i in range(len(numbers2)):
    if(numbers2[i] % 5 == 0):
        print(numbers2[i])

for i in range(len(list3)):
    list4.append(list3[i])
print(list4)

for i in range(len(numbers)):
    if(numbers[i] > maxx):
        maxx = numbers[i]

for i in range(len(numbers2)):
    if(numbers2[i] < minn):
        minn = numbers2[i]
print(minn)

for i in range(len(numbers2)):
    numbers3.append(0)

for i in range(len(numbers2)):
    se = numbers3[i]
    for e in range(len(numbers2)):

        if(i == 0):
            if(se < numbers2[e]):
                se = numbers2[e]
        else:
            if(se < numbers2[e] and numbers2[e] < numbers3[i - 1]):
                se = numbers2[e]
    numbers3[i] = se
print(numbers3)

numbers3 = []

for i in range(len(numbers2)):
    numbers3.append(0)

for i in range(len(numbers2)):
    se = numbers3[len(numbers2) - 1 - i]
    for e in range(len(numbers2)):

        if(i == 0):
            if(se < numbers2[e]):
                se = numbers2[e]
        else:
            if(se < numbers2[e] and numbers2[e] < numbers3[len(numbers2) - i]):
                se = numbers2[e]
    numbers3[len(numbers2) - 1 - i] = se
print(numbers3)

for i in range(6):
    print(i + 1 * 3)

for i in range(3):
    print(i + 1 * 5)

for i in range(10):
    print(10 - i)