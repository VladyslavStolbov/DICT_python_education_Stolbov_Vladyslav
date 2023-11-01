""" Hangman project """
import random

words = ["python", "java", "javascript", "php"]
random_word = random.choice(words)

print("HANGMAN")
print("The game will be available soon.")
guess_word = input("Guess the word:")

if guess_word == random_word:
    print("You survived!")
else:
    print("You lost!")
