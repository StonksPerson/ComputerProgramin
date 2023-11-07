import random
import math

words = open("words.txt")
words = words.readlines()

word = words[math.floor(random.random() * 267751.0)]
revealedWord = ""
loopWord = ""
win = False
tries = 0
maxTries = 10

for i in range(len(word)):
    revealedWord = revealedWord + "_ "

while win == False:

    if(tries > maxTries):
        break
    loopWord = ""
    print(revealedWord)
    guess = input("Type you letter guess, if you think you know what the word is feel free to guess. : ")
    guess = guess.upper()

    if(len(guess) > 1):
        if(guess + " " == word):
            win = True
            break
    else:
        if(word.find(guess) != -1):
            for i in range(len(word) - 1):
                if(word[i] == guess or revealedWord.find(word[i]) > -1):
                    loopWord = loopWord + word[i] + " "
                else: loopWord = loopWord + "_ "
            revealedWord = loopWord
        else: tries += 1


if(win == True):
    print(f'You WIN. The word was: {word}')
else: print(f'You LOST. The word was: {word}')
