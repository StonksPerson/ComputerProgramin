alive = True
player = {'health': 100}
inventory = []
shopBuy = []
shopBuyNames = []
inShop = False
money = 200
event = 0
addMoney = 0
difficulty = 1
specialEvent = ["go to the shop", "shop"]
inventory = [
    {"name": "wood sword", "damage": 5, "durablitity": 5, "obj": 1, "price": 5},
    {"name": "wood sheild", "protection": 5, "durablitity": 20, "obj": 2, "price": 10},
    {"name": "wood armor", "protection": 5, "durablitity": 50, "obj": 3, "price": 15},
    ]
shopItems = [
    {"name": "wood sword", "damage": 5, "durablitity": 5, "obj": 1, "price": 5},
    {"name": "wood sheild", "protection": 5, "durablitity": 20, "obj": 2, "price": 10},
    {"name": "wood armor", "protection": 5, "durablitity": 50, "obj": 3, "price": 15},
    {"name": "iron sword", "damage": 10, "durablitity": 10, "obj": 1, "price": 20},
    {"name": "iron sheild", "protection": 7, "durablitity": 20, "obj": 2, "price": 20},
    {"name": "iron armor", "protection": 10, "durablitity": 50, "obj": 3, "price": 25},
    ]
shopStore = []
distance = 0
move = ""
import random as rand
import math

def movePlayer():
    print()

def runEvent(event, money):
    shopAnswer = ""
    shopStore = []
    shopPrint = ""
    shopBuy = []
    inShop = True
    bought = ""
    
    for i in range(5):
        shopRand = rand.randint(0, len(shopItems) - 1)
        shopStore.append(shopItems[shopRand])
        print(str(i + 1) + " $" + str(shopItems[shopRand]["price"]))
        if shopItems[shopRand]["obj"] == 1 :
            print(shopItems[shopRand]["name"] + " damage: " + str(shopItems[shopRand]["damage"]) + " durability: " + str(shopItems[shopRand]["durablitity"]) + " ")
        elif shopItems[shopRand]["obj"] == 2:
            print(shopItems[shopRand]["name"] + " protectoin: " + str(shopItems[shopRand]["protection"]) + " durability: " + str(shopItems[shopRand]["durablitity"]) + " ")
        else:
            print(shopItems[shopRand]["name"] + " protectoin: " + str(shopItems[shopRand]["protection"]) + " durability: " + str(shopItems[shopRand]["durablitity"]) + " ")
        shopBuy.append(shopItems[shopRand])
        print()

    while inShop == True:

        print(f"You got {bought}")
        print(f"Welcome to the shop! this is our stock {shopPrint}")
        print(f"You have ${money}")
        shopAnswer = input("type the number of what you would like to buy, or type L to leave : ")
        if(shopAnswer.capitalize() == "L"):
            inShop = False
            break
        elif(shopAnswer.isnumeric() and int(shopAnswer) - 1 < len(shopBuy)):
            shopAnswer = int(shopAnswer) - 1
            money = money - shopBuy[shopAnswer]["price"]
            inventory[shopBuy[shopAnswer]["obj"] - 1] = shopBuy[shopAnswer]

            bought = shopBuy[shopAnswer]['name']
            shopBuy2 = []
            for i in range(len(shopBuy)):
                if(i != shopAnswer):
                    shopBuy2.append(shopBuy[i])
            shopBuy = shopBuy2

            for i in range(len(shopBuy)):

                print(str(i + 1) + " $" + str(shopBuy[i]["price"]))
                if shopBuy[i]["obj"] == 1 :
                    print(shopBuy[i]["name"] + " damage: " + str(shopBuy[i]["damage"]) + " durability: " + str(shopBuy[i]["durablitity"]) + " ")
                elif shopBuy[i]["obj"] == 2:
                    print(shopBuy[i]["name"] + " protectoin: " + str(shopBuy[i]["protection"]) + " durability: " + str(shopBuy[i]["durablitity"]) + " ")
                else:
                    print(shopBuy[i]["name"] + " protectoin: " + str(shopBuy[i]["protection"]) + " durability: " + str(shopBuy[i]["durablitity"]) + " ")
                print()
        else: print("Enter a valid number!")
    return money

def enemyBattle():
    words = open("first-names.txt")
    words = words.readlines()
    name = words[math.floor(rand.random() * 4946)]
    enemy = {'health': math.floor(rand.randint(1, 20) * difficulty), 'damage': math.floor(rand.randint(1, 5) * difficulty), "name": name}
    print(f"You encounter an enemy!")
    print()
    inBattle = True
    while inBattle == True:

        print(enemy['name'])
        print(f"hp:[ {enemy['health']} ], strength:[ {enemy['damage']} ]")
        print()
        print(f"you have {player['health']} hp.")
        print()
        action = input("What will you do? (type h for commands): ")
        enemyDamage = enemy["damage"] + rand.randint(-10, 10)
        enemyDamage -= inventory[2]["protection"]
        inventory[2]['durablitity'] -= rand.randint(0,1)

        for i in range(20):
            print()

        if(action.capitalize() == "H"):
            print("a: attack")
            print("d: defend (reduce damage)")
            print("ep: throw potion that can either damage the enemy a lot or heal the enemy a lot")
            print("p: use a potion that can either heal you a lot or damage you")
            print("r: run away (might not work!)")
        elif(action.capitalize() == "A"):
            if inventory[0]['durablitity'] > 0:
                enemy['health'] -= inventory[0]['damage']
                inventory[0]['durablitity'] -= rand.randint(0,1)
            else:
                print("Your sword is broken")
        elif(action.capitalize() == "D"):
            enemyDamage -=  inventory[1]["protection"]
            inventory[1]['durablitity'] -= rand.randint(0,1)
        elif(action.capitalize() == "E"):
            edamage = rand(-10, 10)
            enemy['health'] -= edamage
            print(f'you did {edamage} damage.')
        elif(action.capitalize() == "P"):
            pheal = rand.randint(-10, 10)
            player['health'] += pheal
            print(f'you healed {pheal}.')
        elif(action.capitalize() == "R"):
            run = rand.randint(0,2)
            if(run == 2):
                print("you ran away")
                break
        if(enemy["health"] <= 0):
            addMoney = math.floor(rand.randint(1,20) * difficulty)
            print("You slayed the mosnter!")
            print(f"+ ${addMoney}")
            break



while(alive == True):
    event = rand.randint(0, 100)
    difficulty += 0.01
    move = ""
    move = input(f"Press W to walk forward. To go to the shop press S: ")

    if move.lower() == "w":
        movePlayer()
        distance += 1
        if(event > 90):
            eventPick = rand.randint(0, len(specialEvent) / 2 - 1)
        elif (event < 90 and event > 80):
            randMoney = rand.randint(0, 20)
            print(f"You found ${randMoney}!")
        elif (event < 25):
            enemyBattle()
    elif move.lower() == "s":
        money = runEvent(event, money)       
    elif (move.lower() != ""): 
        print("Invalid input.")



