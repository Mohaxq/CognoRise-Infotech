import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def get_user_choice():
    choice = input("Enter Rock, Paper, or Scissors: ").strip().capitalize()
    while choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid input. Please enter Rock, Paper, or Scissors.")
        choice = input("Enter Rock, Paper, or Scissors: ").strip().capitalize()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to the game of Rock, Paper, Scissors")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Computer's choice is:", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (Yes/No): ").strip().capitalize()
        if play_again != "Yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    play_game()