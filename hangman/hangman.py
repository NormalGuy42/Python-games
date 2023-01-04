from hangman_words import words
import string
import random
import time

HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''',
    
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def get_word():
    #Picks a random word from the list

    word = random.choice(words)
    return word.upper()
#Returns word in all caps

def hangman():
    word = get_word()
    word_letters = set(word)
    #list of letters
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7
    num = 0
    while len(word_letters) > 0 and lives > 0:
        time.sleep(1)
        print(HANGMANPICS[num])
        print("You have used the letters:  ",  " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        if lives > 1:
            print(f"You have {lives} lives left")
        else:
            print(f"You have", 1, "life left")

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print(f"The letter {user_letter} is not in the word")
                lives -= 1
                num += 1
        #When the letter is in used_letters it means it has already been used
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
            time.sleep(0.8)
        else:
            print("Invalid character")
            time.sleep(0.8)
    #The loop is broken when either the word has been guessed or the user has no lives
    if len(word_letters) == 0:
        print("\nYay you guessed the word " + word + " correctly")
    else:
        print(HANGMANPICS[7])
        print(f"\nDamn you lost L, the word was {word}\nBetter luck next time ")

hangman()

