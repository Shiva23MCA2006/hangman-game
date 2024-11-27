import random

from art import logo
from words_list import word_list
from art import stages

print(logo)
chosen_word = random.choice(word_list) 
print(chosen_word) 

word_length = len(chosen_word) 
print(word_length) 

show_blanks = []
lives = 6

for index in range(word_length):
  show_blanks += "_"

print(show_blanks)

isGameEnded = False

while not isGameEnded:
  guess = input("Guess a letter: ").lower()

  if guess in show_blanks:
    print(f"You've already guessed {guess}") 

  for position in range(word_length):
     letter =  chosen_word[position] 

     if letter == guess:
       show_blanks[position] = letter
       
  print(show_blanks)

  if guess not in chosen_word:
    print(f"Unfortunately, your guessed letter {guess} is not present in the word.\nYou lose a life!")
    lives -= 1

    print(f"Reamining lives : {lives}")

    if lives == 0:
      isGameEnded = True
      print("--------You lose. Game Over!!---------")
      print(f"The chosen word was {chosen_word}")

  if "_" not in show_blanks:
    isGameEnded = True
    print("You win!")

  print(stages[lives])
 

