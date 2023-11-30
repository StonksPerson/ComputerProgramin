alive = True
event = 0
specialEvent = ["go to the shop", "shop"]
shopItems = [
    {"name": "wood sword", "damage": 5, "durablitity": 5, "obj": "wepon", "price": 5},
    {"name": "wood sheild", "protection": 5, "durablitity": 20, "obj": "sheild", "price": 10},
    {"name": "wood armor", "protection": 5, "durablitity": 50, "obj": "armor", "price": 15},
    {"name": "iron sword", "damage": 10, "durablitity": 10, "obj": "wepon", "price": 20},
    {"name": "iron sheild", "protection": 7, "durablitity": 20, "obj": "sheild", "price": 20},
    {"name": "iron armor", "protection": 10, "durablitity": 50, "obj": "armor", "price": 25},
    ]
shopStore = []
distance = 0
move = ""
import random as rand

def movePlayer():
    print(">:)")

def runEvent(event):
    shopStore = []
    shopPrint = ""
    for i in range(5):
        shopRand = rand.randint(0, len(shopItems) - 1)
        shopStore.append(shopItems[shopRand])
        print("$" + str(shopItems[shopRand]["price"]))
        if shopItems[shopRand]["obj"] == "wepon" :
            print(shopItems[shopRand]["name"] + " damage: " + str(shopItems[shopRand]["damage"]) + " durability: " + str(shopItems[shopRand]["durablitity"]) + " ")
        elif shopItems[shopRand]["obj"] == "sheild":
            print(shopItems[shopRand]["name"] + " protectoin: " + str(shopItems[shopRand]["protection"]) + " durability: " + str(shopItems[shopRand]["durablitity"]) + " ")
        else:
            print(shopItems[shopRand]["name"] + " protectoin: " + str(shopItems[shopRand]["protection"]) + " durability: " + str(shopItems[shopRand]["durablitity"]) + " ")
        print()


    print(f"Welcome to the shop! this is our stock {shopPrint}")

while(alive == True):
    event = rand.randint(0,1)
    if(event > 0):
        eventPick = rand.randint(0, len(specialEvent) / 2 - 1)
        move = input(f"Press W to walk forward. To {specialEvent[eventPick * 2]} press S: ")
    else:
        move = input("Press W to walk forward: ")
    
    if move.lower() == "w":
        movePlayer()
        distance += 1
    elif move.lower() == "s" and event > 0:
        runEvent(event)
    else: 
        print("Invalid input.")



