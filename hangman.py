import random
import math

words = open("words.txt")
words = words.readlines()

newWord = ""
guessed_letters = ""
guess_word = ""
word = words[math.floor(random.random() * 267751.0)]
for i in range(len(word) - 1):
    newWord = newWord + word[i]
word = newWord
revealedWord = ""
loopWord = ""
win = False
tries = 0
maxTries = 10
guessed_words = []
lastLoop = ""

for i in range(len(word)):
    revealedWord = revealedWord + "_ "

while win == False:

    guessed = 1

    if(tries >= maxTries):
        break

    guess_word = ""
    lastLoop = revealedWord

    loopWord = ""
    guess = input(f"Type you letter guess. you have {maxTries - tries} tries left: ")
    guess = guess.upper()

    if(guessed_words.count(guess) > 0):
        guessed = 0
    else:
        guessed_words.append(guess)
   
    for i in range(len(word)):
        if(word[i] == guess or revealedWord.find(word[i]) > -1):
            
            loopWord = loopWord + word[i] + " "
            guess_word = guess_word + word[i]
        else: loopWord = loopWord + "_ "

    revealedWord = loopWord
    
    if(revealedWord != lastLoop):
        print("Correct guess :)")
        tries -= 1

    if(guessed == 0):
        print("You already guessed that!")
    tries += guessed
    guessed_letters = ""
    for i in range(len(guessed_words)):
        guessed_letters = guessed_letters + guessed_words[i] + ", "

    if(guess_word == word):
        win = True
        break

    print(f"So far you have guessed guessed {guessed_letters}")
    print(revealedWord)
    print(len(guess_word))
    print(len(word))
    print(word)
    

if(win == True):
    print(f'You WIN. The word was: {word}')
else: print(f'You LOST. The word was: {word}')