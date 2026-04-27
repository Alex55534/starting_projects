🎲 Guess the Number Game

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A classic command-line guessing game written in Python. The computer generates a secret number, and the player must deduce it using logic and the remaining attempt count.

## 📑 Table of Contents

- [Features](#-features)
- [How to Run](#-how-to-run)
- [Gameplay Mechanics](#-gameplay-mechanics)
- [Code Structure](#-code-structure)
- [Example Walkthrough](#-example-walkthrough)
- [Customization](#-customization)
- [Dependencies](#-dependencies)
- [License](#-license)

## ✨ Features

- **Random Number Generation**: The computer uses Python's `random` module to select a number between 1 and 10 at the start of each round.
- **Limited Attempts**: Players have exactly **3 attempts** to guess correctly. The remaining attempts are displayed before each input.
- **Input Validation**: Includes robust error handling to prevent crashes if the user accidentally types letters or symbols instead of numbers.
- **Dynamic Feedback**: Upon winning, the game randomly selects a congratulatory message from a list of fun phrases:
  - `"Yes, we won"`
  - `"You are so great, this is the right answer."`
  - `"You clearly have the gift of clairvoyance."`
- **Replay Loop**: After a win or loss, the player is prompted to play another round without restarting the script.

## 🚀 How to Run

Follow these steps to get the game running on your local machine:

### Prerequisites
- **Python**: Version 3.6 or newer. You can check your version by running `python --version` or `python3 --version` in your terminal.

### Installation & Execution
1. **Clone the repository** (or download the script file directly):
   ```bash
   git clone https://github.com/your-username/guess-the-number.git
   cd guess-the-number

Run the script:

bash
python main.py

🕹️ Gameplay Mechanics

The game loop operates as follows:

Initialization: The script imports random and greets the user with "Good afternoon".

User Consent: The user is asked "You want to play this game? Yes/No?".

If "No": The program prints "Best wishes" and exits.

If "Yes" (or anything other than "No" at startup): The game proceeds with "Fine, Let's go".

The Guessing Phase:

The computer secretly selects a number (randomat).

The user has 3 attempts (num < 3).

Valid Input: The user must enter an integer. If they enter text, a ValueError is caught, and they are prompted "You can't enter this letters" without losing an attempt.

Winning: If the guess matches the secret number, a random victory phrase is printed, and the inner loop breaks.

Losing: If 3 incorrect guesses are made, the message "Ohh, sorry, but you lose" is printed.

Post-Round: The user is asked "Do you want playing again? Yes/No".

If "Yes": The outer while True loop resets, generating a new number and restoring 3 attempts.

If "No": The program prints "Good wishes" and terminates.

📝 Example Walkthrough

Good afternoon
You want to play this game? Yes/No? Yes
Fine, Let's go
I give you a number from 1 to 10, and you need to guess it.
You have left 3 attempts 5
You have left 2 attempts 8
You are so great, this is the right answer.
Do you want playing again? Yes/No Yes
Fine, Let's go
I give you a number from 1 to 10, and you need to guess it.
You have left 3 attempts 1
You have left 2 attempts 2
You have left 1 attempts 3
Ohh, sorry, but you lose
Do you want playing again? Yes/No No
Good wishes



