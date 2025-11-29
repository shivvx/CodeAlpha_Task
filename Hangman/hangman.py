import random
def play_hangman():
    word_list = ["apple", "grape", "mango", "berry", "peach"]
    secret_word = random.choice(word_list)
    lives = 6
    guessed_letters = []

    print("--- WELCOME TO HANGMAN ---")
    while lives > 0:
        display_word = ""
        letters_missing = 0
        
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                letters_missing += 1
        
        print(f"\nWord: {display_word}")
        print(f"Lives left: {lives}")
        if letters_missing == 0:
            print("\nYOU WON! You guessed the word!")
            break
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that!")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            lives -= 1
            print(f"Sorry, '{guess}' is not there.")
    if lives == 0:
        print(f"\nGAME OVER! The word was: {secret_word}")

play_hangman()