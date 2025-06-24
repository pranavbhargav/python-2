# python-2
internship on python
import random

# List of words to choose from
word_list = ['python', 'hangman', 'challenge', 'programming', 'developer']

# Randomly select a word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize variables
display = ['_'] * word_length
guessed_letters = []
lives = 6

print("Welcome to Hangman!")
print(' '.join(display))

# Main game loop
while lives > 0 and '_' in display:
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue

    guessed_letters.append(guess)

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        print(' '.join(display))
    else:
        lives -= 1
        print(f"Incorrect guess. You have {lives} lives remaining.")
        print(' '.join(display))

# Check if the player has won or lost
if '_' not in display:
    print("Congratulations! You guessed the word correctly.")
else:
    print(f"Game over. The word was '{chosen_word}'.")
