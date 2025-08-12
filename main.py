# main.py

import random

# load words from file
f = open("data/words.txt", "r")
words_list = []
for line in f:
    words_list.append(line.strip())
f.close()

secret_word = random.choice(words_list)

max_attempts = 6
attempts = 0
win = False

while attempts < max_attempts:
    guess = input("Enter a 5 letter word: ").lower()
    if len(guess) != 5:
        print("Word must be 5 letters!")
        continue
    if guess not in words_list:
        print("Word not in list!")
        continue

    result = ["_"] * 5
    temp_secret = list(secret_word)

    # mark correct letters first
    for i in range(5):
        if guess[i] == secret_word[i]:
            result[i] = guess[i].upper()
            temp_secret[i] = "*"

    # mark present letters
    for i in range(5):
        if result[i] == "_":
            if guess[i] in temp_secret:
                result[i] = guess[i]
                temp_secret[temp_secret.index(guess[i])] = "*"

    print("Result:", " ".join(result))

    attempts = attempts + 1

    if guess == secret_word:
        win = True
        break

if win:
    print("You Win! The word was:", secret_word)
else:
    print("You Lose! The word was:", secret_word)
