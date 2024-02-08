import random

logo = """   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
                                                                                          """

#Starting of the Game
print(logo)
print("Welcome to the Number Guessing Game! \n")
print("Guess a number between 1 and 100. \n")

tries = 10
#Flag to track the win
win = False
answer = random.randint(1, 100)
# print(f"Pssst, the correct answer is {answer}\n")
#Choosing the difficulty level
difficulty = input("Choose a difficulty. Type 'easy' or 'hard. \n")

if difficulty == "hard":
    tries = 5

#Looping through the guesses
while tries > 0:
    print(f"You have {tries} attempts remaining to guess the number. \n")
    guess = int(input("Make a guess: \n"))

    if guess == answer:
        win = True
        break
    elif guess < answer:
        print("Too low. \n")
    else:
        print("Too high. \n")

    tries -= 1
    if tries == 0:
        break
    else:
        print("Guess again. \n")

#Printing the final status of the game
if win == True:
    print("You Won Hurrayy!!! \n")
else:
    print("Try Again You Lose....\n")
