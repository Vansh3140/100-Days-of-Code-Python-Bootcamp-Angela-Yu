import random
import hangman_words as words
import hangman_art as art

chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess and display[position] == "_":
            display[position] = letter
        elif letter == guess:
            print(f"You have already guessed {guess}")

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not present in the word. Try Again !!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!!!! \nGame Over")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!!!! \nGame Over")

    print(art.stages[lives])
