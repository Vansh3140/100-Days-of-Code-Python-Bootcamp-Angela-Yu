rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to Rock, Paper ,Scissors Game....")

num1=int(input("What do you choose? Type 0 for Rock,1 for Paper and 2 for Scissors.\n"))

num2=random.randint(0,2)

if num1==0:
  print(rock)
elif num1==1:
  print(paper)
else:
  print(scissors)

print("Computer chose:")

if num2==0:
  print(rock)
elif num2==1:
  print(paper)
else:
  print(scissors)


if num1==0 and num2==1:
  print("You lose")
elif num1==0 and num2==2:
  print("You win")
elif num1==num2:
  print("It's a draw")
elif num1==1 and num2==0:
  print("You win")
elif num1==1 and num2==2:
  print("You lose")
elif num1==2 and num2==0:
  print("You lose")
else:
  print("You won")