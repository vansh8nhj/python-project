import random

def coin_toss():
    """Simulates a coin toss."""
    return random.choice(['Heads', 'Tails'])

def main():
    print("Welcome to the Coin Toss Game!")
    print("I will flip a coin, and you will guess if it's 'Heads' or 'Tails'.")

    while True:
        guess = input("Enter your guess ('Heads' or 'Tails'), or 'quit' to end the game: ").capitalize()
        if guess == 'Quit':
            print("Thanks for playing! Goodbye!")
            break
        elif guess not in ['Heads', 'Tails']:
            print("Invalid input! Please enter 'Heads' or 'Tails'.")
            continue
        
        result = coin_toss()
        print("The coin shows:", result)
        if result == guess:
            print("Congratulations! You guessed it right!")
        else:
            print("Sorry, you guessed it wrong.")
if __name__ == "__main__":
    main()