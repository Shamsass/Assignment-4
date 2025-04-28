# Welcome to the High-Low Game!
# --------------------------------
# Round 1
# Your number is 8
# Do you think your number is higher or lower than the computer's?: lower
# You were right! The computer's number was 35
# Your score is now 1

# Round 2
# Your number is 88
# Do you think your number is higher or lower than the computer's?: higher
# Aww, that's incorrect. The computer's number was 100
# Your score is now 1

# Round 3
# Your number is 63
# Do you think your number is higher or lower than the computer's?: higher
# You were right! The computer's number was 5
# Your score is now 2

# Round 4
# Your number is 57
# Do you think your number is higher or lower than the computer's?: lower
# Aww, that's incorrect. The computer's number was 57
# Your score is now 2

# Round 5
# Your number is 22
# Do you think your number is higher or lower than the computer's?: lower
# Aww, that's incorrect. The computer's number was 1
# Your score is now 2

# Thanks for playing!
import random

print("Welcome to the High-Low Game!")
print("--------------------------------")

score = 0
rounds = 5

for round_number in range(1, rounds + 1):
    print(f"Round {round_number}")
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    print(f"Your number is {player_number}")
    
    guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

    if player_number == computer_number:
        print(f"It's a tie! Both numbers were {player_number}")
        print(f"Your score remains {score}")
    else:
        correct_guess = ""
        if player_number > computer_number:
            correct_guess = "higher"
        else:
            correct_guess = "lower"
        
        if guess == correct_guess:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}\n")

print("Thanks for playing!")
print(f"Your final score was: {score}")
