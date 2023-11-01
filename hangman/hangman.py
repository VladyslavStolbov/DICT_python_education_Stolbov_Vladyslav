""" Hangman project """
import random

words = ["python", "java", "javascript", "php"]
random_word = random.choice(words)
hint_word = random_word[:3] + "-" * (len(random_word) - 3)
print("HANGMAN")
print("The game will be available soon.")
guess_word = input(f"Guess the word {hint_word}:")

if guess_word == random_word:
    print("You survived!")
else:
    print("You lost!")
