word = "awesome"
revealedWord = "_ _ _ _ _ _"
loopWord = ""
win = False


while win == False:
    loopWord = ""
    guess = input("Type you letter guess, if you think you know what the word is feel free to guess. : ")
    if(len(guess) > 1):
        if(guess == word):
            win = True
            break
    else:
        if(word.find(guess) != -1):
            for i in range(len(word)):
                if(word[i] == guess or revealedWord.find(word[i]) > -1):
                    loopWord = loopWord + word[i] + " "
                else: loopWord = loopWord + "_ "
            revealedWord = loopWord
    print(revealedWord)
           
print(f'You WIN. The word was: {word}')
