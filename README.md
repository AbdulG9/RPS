# Rock Paper Scissors Game in Python

A simple implementation of the classic **Rock, Paper, Scissors** game written in Python. In this game, you can play against the computer, with the computer's choices being made randomly. The game tracks your wins, losses, and ties, and it continues until you choose to quit.

## Features
- **Command-line Interface (CLI)**: A simple and user-friendly terminal interface.
- **Single Player Mode**: Play against the computer.
- **Score Tracking**: Keeps track of the number of wins, losses, and ties.
- **Random Computer Choices**: The computer makes random choices from Rock, Paper, or Scissors.

## Installation

To get started with the game, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rock-paper-scissors.git
2. Navigate into the project directory:
   ```bash
   cd rock-paper-scissors
3. Run the game:
   ```bash
   python rock_paper_scissors.py
## How to Play
1. When the game starts, you'll be prompted to choose between Rock, Paper, or Scissors.
2. After making your choice, the computer will randomly select one of the three options.
3. The game will determine the winner based on the following rules:
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
4. The score will be displayed after each round, showing the number of wins, losses, and ties.
5. You can keep playing as long as you want or exit the game anytime.

## Example Gameplay
```bash
*** ROCK PAPER & SCISSORS GAME ***
Choose
 r-ROCK
 p-PAPER
 s-SCISSORS
 e-EXIT

Enter your choice : r
computer choose: SCISSORS
you choose: ROCK
YOU got a point!!!
SCORES:
 you: 1 computer: 0
Enter your choice : r
computer choose: PAPER
you choose: ROCK
Computer got a point!
SCORES:
 you: 1 computer: 1
Enter your choice : s
computer choose: ROCK
you choose: SCISSORS
computer got a point!
SCORES:
 you: 1 computer: 2
Enter your choice : e
*** YOU LOST THE GAME WITH 1 points***
game exited succesfully!!!
