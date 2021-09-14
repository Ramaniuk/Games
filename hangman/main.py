import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in range(word_length):
  display.append("_")

while "_" in display:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You've already guessed{guess}")
  
  if guess in chosen_word:
    for position in range(word_length):
      if guess == chosen_word[position]:
        display[position] = guess
        print(f"{' '.join(display)}")
  else:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    print(hangman_art.stages[lives])
  
  if lives == 0:
    break

if "_" not in display:
  print ("You win.")
else:
  print("You loose")
