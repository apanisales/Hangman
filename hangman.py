#Author: Anthony Panisales

import random

def playHangman(word):
    chances = 5
    correctLetters = []
    wrongLetters = []
    while chances > 0:
        for i in range(len(word)):
            if word[i] in correctLetters:
                print(word[i], end=" ")
            else:
                print("_", end=" ")
        print()
        if not len(correctLetters) == 0:
            print()
            wantToGuess = str.lower(input("Do you want to make a guess?(y/n) "))
            while wantToGuess != "y" and wantToGuess != "n":
                wantToGuess = str.lower(input("Do you want to make a guess?(y/n) "))
            if wantToGuess == "y":
                playerGuess = str.lower(input("What is your guess? "))
                if playerGuess == word:
                    print("Correct! Good job!")
                    break
                else:
                    print("Wrong!")
        print("You have " + str(chances) + " chances")
        if not len(wrongLetters) == 0:
            print("Wrong Letters: [", end= "")
            for w in wrongLetters:
                if w != None:
                    print(w, end=" ")
            print("]", end="")
        letter = str.lower(input("\n" + "Pick a letter: "))
        if len(letter) > 1:
            print("You can only input single letters")
        else:
            if letter in word:
                if letter in correctLetters:
                    print("You have already guessed this letter")
                else:
                    correctLetters.append(letter)
            else:
                if letter in wrongLetters:
                    print("You have already guessed this letter")
                else:
                    print("Wrong!")
                    wrongLetters.append(letter)
                    chances = chances - 1
                    if chances == 0:
                        print("You lose! The word was '" + word + "'")

    print()


def handleFile():
    hangmanList = []
    filename = "hangmanWords.txt"
    file = open(filename, "r")
    for line in file:
        #Makes sure that the words are at least three letters and are not names
        if not str.isupper(line[:1]):
            if len(line) > 2:
                hangmanList.append(line.replace('\n', ""))
    file.close()
    return hangmanList

def main():
    hangmanList = handleFile()
    play = "y"
    while play == "y":
        print("Let's play hangman!")
        choice1 = str.lower(input("Are you playing with others?(y/n) "))
        while choice1 != "y" and choice1 != "n":
            choice1 = str.lower(input("Are you playing with others?(y/n) "))
        print()
        if choice1 == "y":
            print("Choose if you want to pick a word for someone else to solve. " + "\n" +
            "If you choose no, then a word is randomly selected for you to play with." + "\n" +
            "Warning: These randomly selected words can be hard to solve!")
            choice2 = str.lower(input("Do you want to use your own word?(y/n) "))
            while choice2 != "y" and choice2 != "n":
                choice2 = str.lower(input("Do you want to use your own word?(y/n) "))
            print()
            if choice2 == "y":
                print("The word you choose has to be an actual English word")
                yourWord = input("What is your word? ")
                while yourWord not in hangmanList:
                    print("That's not a real word!")
                    yourWord = input("What is your word? ")
                    print()
                for i in range(150):
                    print()
                playHangman(yourWord)
            else:
                index = random.randint(0, len(hangmanList))
                word = hangmanList[index]
                playHangman(word)
        else:
            print("A random word will be chosen for you" + "\n"
                  "Warning: These randomly selected words can be hard to solve!")
            index = random.randint(0, len(hangmanList))
            word = hangmanList[index]
            playHangman(word)
        play = str.lower(input("Do you want to play another game?(y/n) "))
        while play != "y" and play != "n":
            play = str.lower(input("Do you want to play another game?(y/n) "))
        print()
    print("\n" + "Thanks for playing!")

main()
