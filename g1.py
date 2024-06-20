import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while attempts > 0:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
        
        current_display = display_word(word, guessed_letters)
        print(current_display)
        
        if '_' not in current_display:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Game over! The word was '{word}'.")
        
    if input("Play again? (yes/no): ").lower() == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
