import random

#choosing the words
def choose_word():
    word_list = ["python", "hangman", "game", "codalpha","programming", "computer"]
    return random.choice(word_list)

#display the guessed letter by the user
def display_word(word, guessed_letters):
    display = "  "
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

#Main hangman game 

def hangman():
    word = choose_word()
    guess_letters = [ ]
    incorrect_guesses = 0
    max_attempts = 6

    print("\n")
    print(" Welcome to Play HANGMAN Game ")
    print(display_word(word, guess_letters))

    while (incorrect_guesses < max_attempts):
        guess = input("Guess a letter: ").lower()

    

        if guess in guess_letters:
            print("You've already guessed that letter.")
            print("\n")
            continue

        guess_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print("Incorrect Guess " +str(max_attempts - incorrect_guesses)+ " Attempts Left.")
            print("\n")
        
        else:
            print("Correct Guess ")
            print("\n")

        print(display_word(word, guess_letters))

        if "_" not in display_word(word, guess_letters):
            print("Congratulations , You've Guessed the Word Correctly!")
            print(" WINNER ")
            break

    else:
        print("Sorry, You ran out of Attempts. The Word is "+str(word))
        print("TRY AGAIN")

hangman()
