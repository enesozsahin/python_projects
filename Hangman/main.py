import random
from WordList import wordlistfinal
from hangman_art import *


print(logo +'\n' +Info)

word=random.choice(wordlistfinal)

list=[]
for x in range(len(word)):
    list += '_'
def importoutput():
    for x in list:
        print(x,end=" ")

lives=6
importoutput()
guesslist=[]
print(stages[lives])
while True:
    while True:
        guess = input("\n\nGuess a letter > ").upper()

        if len(guess) >1:
            print("PLEASE WRITE ONLY ONE LETTER ONCE")
        elif guess.isalpha()==False:
            print("PLEASE WRITE A LETTER")
        else:
            break

    if guess not in word:
        if guess not in guesslist:
            lives=lives-1
            print(stages[lives])

    if guess in guesslist:
        print(f"You used {guess} before")
    else:
        guesslist+=guess


    for a in range(len(word)):
        letter = word[a]
        if letter==guess:
            list[a]=letter

    if "_" not in list:
        print(f'You guessed the word {word}!')
        print("**YOU WIN**")
        break

    if lives==0:
        print("GAME OVER")
        print(f'The word was {word}!')
        break


    print(f"You have {lives} guesses left")

    importoutput()
    print(f'\nUsed letters:{guesslist}')