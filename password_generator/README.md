# 🔐 Password Generator

A simple command-line password generator written in Python. It allows you to create secure passwords with customizable character sets and includes convenient repeat-generation loops.

## 🚀 Features

- **All Characters Mode (Option 2)**: Generates a password using lowercase letters, uppercase letters, digits, and punctuation. After generation, you can instantly create more passwords of the same type without returning to the main menu.
- **Custom Mode (Option 1)**: Choose from predefined combinations:
  1. Letters and numbers
  2. Numbers and special characters
  3. Special characters and letters
  4. Numbers only
  5. Special characters only
  6. Letters only
- **Repeat Generation**: Inside each mode, you are prompted to generate another password without re‑entering the length or method.
- **Input Validation**: Prevents crashes from non‑numeric input and ensures length is positive.

## 📦 Requirements

- Python 3.6 or higher
- No external libraries needed (uses only built-in modules: `random`, `string`)

## 🛠️ How to Run

1. Clone this repository or download the script.
2. Open a terminal in the project folder.
3. Run the script:
   ```bash
   python password_generator.py

🕹️ Usage Example

Select a password creation method (Custom = 1, All characters together = 2) Press 0 to exit the program 2

Enter length 12

x9F#kL2@mP&z

 Password Generated

Generated more: yes/no yes

G7$bN3^pL8qR

 Password Generated

Generated more: yes/no no

Exit

Select a password creation method (Custom = 1, All characters together = 2) Press 0 to exit the program 1

Enter length 8

 letters and numbers - 1, numbers and special characters - 2, special characters and letters - 3, only numbers - 4, only special characters - 5, only letters - 6

Select a password creation method 1

aB3dE9gH

 The password has been generated

Generate more? (yes/no): yes

 letters and numbers - 1, numbers and special characters - 2, special characters and letters - 3, only numbers - 4, only special characters - 5, only letters - 6

Select a password creation method 3

K#mP&zLq

 The password has been generated

Generate more? (yes/no): no

Exit.

Select a password creation method (Custom = 1, All characters together = 2) Press 0 to exit the program 0
