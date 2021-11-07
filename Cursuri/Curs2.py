from list_of_words import get_random_word

# Hangman
MAX_TRIES = 7
try_count = 0
word_to_guess = get_random_word()
letters_guessed = {word_to_guess[0], word_to_guess[-1]}  # First and last letters are visible


def word_to_list(word, letters):
    out_list = list()
    for c in word:
        if c in letters:
            out_list.append(c)
        else:
            out_list.append("_")
    return out_list


while try_count < MAX_TRIES:
    sorted(letters_guessed)
    guessed_word = word_to_list(word_to_guess, letters_guessed)
    print(" ".join(guessed_word))
    if guessed_word.count("_") == 0:
        break
    letter = input("Introdu o litera: ")[0].lower()
    if not letter.isalpha():
        print("Te rog sa introduci o litera!")
    elif letter in letters_guessed:
        print("Litera aceasta este deja vizibila")
        print(f"Litere vizibile: {letters_guessed}")
    else:
        letters_guessed.add(letter)
        if letter not in word_to_guess:
            try_count += 1


if try_count >= MAX_TRIES:
    print("Ai pierdut :(")
    print(f"Cuvantul a fost: {word_to_guess}")
else:
    print("Ai castigat :)")
