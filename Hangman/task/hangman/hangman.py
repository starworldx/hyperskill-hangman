import random

print("H A N G M A N\n")

rand_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
hidden_word = ''

for char in rand_word:
    hidden_word += '-'

hidden_word_list = list(hidden_word)
tries = 0

while tries < 8:
    print("\n"+hidden_word)
    guess = input("Input a letter: ")
    if guess not in rand_word:
        print("No such letter in the word")
    else:
        for i in range(len(rand_word)):
            if rand_word[i] == guess:
                hidden_word_list[i] = guess
    hidden_word = ''.join(str(char) for char in hidden_word_list)
    tries += 1

print("\nThanks for playing!")
