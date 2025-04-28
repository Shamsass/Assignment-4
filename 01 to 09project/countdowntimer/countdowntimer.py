import random

words_list = ["code", "python", "hangman"]

def display_word(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
        display += " "
    return display.strip()

word = random.choice(words_list)

def hangman():
    guessed_letters = set()
    attempts = 6
    while attempts > 0:
        print("-" * 20)
        print("Welcome to Hangman Game")
        print(f"Word: {display_word(word=word, guessed=guessed_letters)}")
        print(f"Guessed Letters: {' '.join(sorted(guessed_letters))}")
        print(f"Remaining Attempts: {attempts}")

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations, you won!")
            print(f"The word was: {word}")
            break
    else:
        print("\nYou failed!")
        print(f"The word was: {word}")

if __name__ == "__main__":
    hangman()
