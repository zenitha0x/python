import random

def generate_word():
    words = ["python", "programming", "hello", "world", "computer"]
    return random.choice(words)

def get_guess():
    return input("Guess a letter: ")

def check_guess(word, guess):
    if guess in word:
        return True
    else:
        return False

def play_hangman():
    word = generate_word()
    guessed_letters = []
    lives = 6

    while lives > 0:
        print("The word is: ", end="")
        for letter in word:
            if letter in guessed_letters:
                print(letter, end="")
            else:
                print("-", end="")

        guess = get_guess()

        if check_guess(word, guess):
            guessed_letters.append(guess)
        else:
            lives -= 1

        if lives == 0:
            print("You lose!")
        else:
            print("You have", lives, "lives left.")

    if lives > 0:
        print("You win!")

if __name__ == "__main__":
    play_hangman()
