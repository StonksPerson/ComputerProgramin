player_1 = input("Player 1: Rock, Paper, or Scissors: ")
for i in range(50):
    print()
player_2 = input("Player 2: Rock, Paper, or Scissors: ")



def one():
    print("Player 1 Wins")

def two():
    print("Player 2 Wins")

if(player_1 == player_2):
    print("It was a tie")

if(player_1 == 'Scissors' and player_2 == 'Rock'):
    two()
elif(player_1 == 'Scissors' and player_2 == 'Paper'):
    one()
elif(player_1 == 'Paper' and player_2 == 'Scissors'):
    two()
elif(player_1 == 'Paper' and player_2 == 'Rock'):
    one()
elif(player_1 == 'Rock' and player_2 == 'Paper'):
    two()
elif(player_1 == 'Rock' and player_2 == 'Scissors'):
    one()