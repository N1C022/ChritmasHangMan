# A program to play the classic game of Hangman with a Christmas twist!

# ----------------
# Import libraries
# ----------------
import random

# ----------------
# Constants
# ----------------
HANGMAN_PICS = ['''
     *
    /.\\
   /..'\\
  /.''.'\\
  /.'.'.\\
 /'.''.'.\\
 ^^^[_]^^^
''', '''

    /.\\
   /..'\\
  /.''.'\\
  /.'.'.\\
 /'.''.'.\\
 ^^^[_]^^^''', '''


   /..'\\
  /.''.'\\
  /.'.'.\\
 /'.''.'.\\
 ^^^[_]^^^''', '''



  /.''.'\\
  /.'.'.\\
 /'.''.'.\\
 ^^^[_]^^^''', '''




  /.'.'.\\
 /'.''.'.\\
 ^^^[_]^^^''', '''





 /'.''.'.\\
 ^^^[_]^^^''', '''






    [_]''']


WORDS = ["carol", "angel", "reindeer", "christmas", "bells", "holly", "elf", "snowball", "candycane", "cocoa", "tinsel", "frost", "wreath", "gingerbread", "nutcracker", "sleigh", "cookie", "holly", "mistletoe"]

alphabet = "abcdefghijklmnopqrstuvwxyz"


# ----------------
# Subprograms
# ----------------


def choose_random_word(): # This chooses a random word from WORDS to be the secret word
    return random.choice(WORDS)

def display_image(pic_num): # Displays the christmas Tree in HANGMAN_PICS
    print(HANGMAN_PICS[pic_num])

def play_game(): #Main subprogram that plays the game and interacts with user
    secret_word = choose_random_word()
    secret_word_list = [letter for letter in secret_word] #converts secret_word into a list
    display_image(0),
    correct_letters = ["_"]*len(secret_word) #Creates a list of correct letters currently just _ as none yet
    incorrect_letters = 0
    already_guessed = []

    while incorrect_letters < len(HANGMAN_PICS) - 1:
        print(" ".join(correct_letters))
        print("Incorrect letters guessed so far:", " ".join(already_guessed))
        letter = input("Enter a letter: ").lower()
        while letter not in alphabet:
            print("please enter a valid letter")
            letter = input("Enter a letter: ").lower()

        if letter in already_guessed or letter in correct_letters:
            print("You have already guessed that letter!")
        elif letter in secret_word:
            print("Correct!", letter, "is in the secret word!")
            for x in range(len(secret_word)):
                if secret_word[x] == letter:
                    correct_letters[x] = letter
            print(" ".join(correct_letters))
            if secret_word_list == correct_letters:
                display_image(0)
                print("Congratulations! You've won the game!")
                break
        else:
            print("Sorry,", letter, "is not in the secret word!")
            incorrect_letters += 1
            already_guessed.append(letter)

        display_image(incorrect_letters)

    if incorrect_letters == len(HANGMAN_PICS) - 1:
        print("Sorry, you've run out of guesses!")
        print("The secret word was:", secret_word)

# ----------------
# Main program
# ----------------

print("Welcome to Christmas Hangman! Try to guess the secret word!")
play_game()
