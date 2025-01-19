import random

# Dictionary of possible moves with corresponding numbers
moves = {1: 'rock', 2: 'paper', 3: 'scissors'}

# Function to determine the winner
def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It's a tie!"
    elif (player_move == 'rock' and computer_move == 'scissors') or \
         (player_move == 'scissors' and computer_move == 'paper') or \
         (player_move == 'paper' and computer_move == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Main loop
def main():
    while True:
        print("\nOptions: [1] Rock, [2] Paper, [3] Scissors, [0] Exit")
        
        try:
            # Get the player's choice as a number
            player_choice = int(input("Enter your choice (1, 2, 3 or 0 to exit): "))
            
            if player_choice == 0:
                print("Thanks for playing!")
                break
            elif player_choice not in moves:
                print("Invalid choice! Please try again.")
            else:
                player_move = moves[player_choice]
                # Computer makes a move
                computer_move = random.choice(list(moves.values()))
                print(f"Computer chose: {computer_move}")

                # Determine the winner
                result = determine_winner(player_move, computer_move)
                print(result)
        
        except ValueError:
            print("Please enter a valid number (1, 2, 3 or 0).")

# Run the game
if __name__ == "__main__":
    main()
