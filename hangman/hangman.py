""" Hangman project """
word = "python"

print("HANGMAN")
print("The game will be available soon.")
guess_word = input("Guess the word:")

if guess_word == word:
    print("You survived!")
else:
    print("You lost!")
