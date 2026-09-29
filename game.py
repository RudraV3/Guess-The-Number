import random

print("Welcome to the number guessing game!")
print("The rules of this game are simple: try to guess the number") 
print("within 10 tries.")
print("Let's see how good you are at guessing!")
print(" ")

def difficulty():
    while True:
        intensity = input("Pick a difficulty: easy, medium, or hard: ").strip().lower()
        if intensity == "easy":
            print("You selected Easy mode.")
            print(" ")
            return "easy"
        elif intensity == "medium":
            print("You selected Medium mode.")
            print(" ")
            return "medium"
        elif intensity == "hard":
            print("You selected Hard mode.")
            print(" ")
            return "hard"
        else:
            print("That is not a valid difficulty. Please try again.")

while True:
    chosen_difficulty = difficulty()

    if chosen_difficulty == "easy":
        max_range = 1000
    elif chosen_difficulty == "hard":
        max_range = 10000
    else:
        max_range = 5000

    secret_number = random.randint(1, max_range)
    
    tries = 10 

    while tries > 0:
        try: 
            guess = int(input(f"Guess a number from 1 to {max_range}: "))
        except ValueError:
            print(" ")
            print("Please enter a valid integer.")
            continue
        
        if guess < 1 or guess > max_range:
            print(" ")
            print(f"Out of bounds! Please enter a number between 1 and {max_range}.")
            print(f"You still have {tries} guesses left.")
            print(" ")
            continue
        
        if guess < secret_number:
            print("Incorrect! The number is higher.")
            tries -= 1
            print("You now have " + str(tries) + " guesses left.")
            print(" ")
            
        elif guess > secret_number:
            print("Incorrect! The number is lower.")
            tries -= 1
            print("You now have " + str(tries) + " guesses left.")
            print(" ")
            
        else:
            print("Correct! You guessed the number!")
            print(" ")
            break 

        if tries == 0:
            print(f"You lost the game. The number was {secret_number}.")
            print(" ")
            break 

    play_again = input("Would you like to play again? ").strip().lower()
    
    if play_again in ["yes", "yeah", "ye", "yea"]:
        print(" ")
        print("Great! Resetting the game...")
        print(" ")
        continue
        
    elif play_again in ["no", "nope", "nah"]:
        print(" ")
        print(" ")
        print("Okay, thank you for playing! Have a great rest of your day!")
        print("- Rudra Vaja")
        break