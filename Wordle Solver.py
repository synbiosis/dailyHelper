import random

#all possible words
with open("5 letter words.csv", "r") as file:
    wordle = random.choice(file.read().split('","'))

    print(list(wordle))


#You have 6 tries to guess
    def solver(wordle):
        guess = ""
        counter = 0
        while guess != wordle:
            guess = input()
            while len(guess) != 5:
                guess = input("Please enter a five letter word \n")
            for counter, letter in enumerate(list(wordle)):
                if guess[counter] == letter:
                    print(letter + " is in the word in the right spot")
            for letter in guess:
                if letter in wordle:
                    print(letter + " is in the word, but the wrong spot")
            print("Try again")
            counter += 1
            if counter >= 6:
                print("You failed")
                return None
        print("You win!")


    solver(wordle)
