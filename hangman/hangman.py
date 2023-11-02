""" Hangman project """
import random

MAX_ATTEMPTS = 8

words = ["python", "java", "javascript", "php"]
word_to_guess = random.choice(words)
display_word = ["-"] * len(word_to_guess)
attempts = 0

print("HANGMAN")
print("The game will be available soon.")

while attempts < MAX_ATTEMPTS:
    print("".join(display_word))
    letter = input("Input a letter:")

    if letter in word_to_guess and letter not in display_word:
        for i in range(len(word_to_guess)):
            if letter in word_to_guess[i]:
                display_word[i] = letter
    else:
        print("That letter doesn't appear in the word")
        attempts += 1

    if "".join(display_word) == word_to_guess:
        print("Thanks for playing!\nWe'll see how well you did in the next stage")

    if attempts == MAX_ATTEMPTS:
        print("Thanks for playing!\nWe'll see how well you did in the next stage")
