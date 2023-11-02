""" Hangman project """
import random

MAX_ATTEMPTS = 8

words = ["python", "java", "javascript", "php"]
word_to_guess = random.choice(words)
display_word = ["-"] * len(word_to_guess)
attempts = 0
used_letters = []
guessed_letters = []

print("HANGMAN")
print("The game will be available soon.")

while attempts < MAX_ATTEMPTS:
    print("".join(display_word))
    letter = input("Input a letter:")

    if letter in (guessed_letters or used_letters):
        print("You've already guessed this letter.")
        continue

    if not letter.encode().isalpha() or not letter.islower():
        print("Please enter a lowercase English letter.")
        continue

    if len(letter) != 1:
        print("You should input a single letter.")
        continue

    used_letters.append(letter)

    if letter in word_to_guess:
        if letter not in display_word:
            for i in range(len(word_to_guess)):
                if letter in word_to_guess[i]:
                    display_word[i] = letter
    else:
        print("That letter doesn't appear in the word")
        attempts += 1

    guessed_letters.append(letter)

    if "".join(display_word) == word_to_guess:
        print(f"You guessed the word {word_to_guess}!\nYou survived")
        break

    if attempts == MAX_ATTEMPTS:
        print("You lost!")
        break
