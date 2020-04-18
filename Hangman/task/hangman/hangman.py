import random, sys

print("H A N G M A N\n")

while True:
    act = input('Type "play" to play the game, "exit" to quit:')
    if act == 'exit':
        sys.exit(0)
    elif act != 'play':
        continue

    rand_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
    hidden_word = ''

    for char in rand_word:
        hidden_word += '-'

    hidden_word_list = list(hidden_word)
    tries = 0
    guessed = []

    while tries < 8:
        print("\n" + hidden_word)
        guess = input("Input a letter: ")

        if guess in guessed:
            print("You already typed this letter")
            continue
        elif len(guess) > 1 or len(guess) == 0 or ' ' in guess:
            print("You should print a single letter")
        elif not guess.isalpha() or not guess.islower():
            print("It is not an ASCII lowercase letter")
        elif guess not in rand_word:
            print("No such letter in the word")
            guessed.append(guess)
            tries += 1
        else:
            guessed.append(guess)
            for i in range(len(rand_word)):
                if rand_word[i] == guess:
                    hidden_word_list[i] = guess

        hidden_word = ''.join(str(char) for char in hidden_word_list)

    if '-' in hidden_word:
        print("You are hanged!")
    else:
        print("You survived!")
    continue


