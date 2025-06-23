import random

def get_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'automation']
    return random.choice(words).upper()

def display(word, guessed):
    return ' '.join([letter if letter in guessed else '_' for letter in word])

def hangman():
    word = get_word()
    guessed = set()
    tries = 6

    print("Welcome to Hangman!")
    print(display(word, guessed))

    while tries > 0 and set(word) != guessed:
        guess = input("Guess a letter: ").upper()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if guess in guessed:
            print("You already guessed that letter.")
            continue
        if guess in word:
            guessed.add(guess)
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong! Tries left: {tries}")
        print(display(word, guessed))

    if set(word) == guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()