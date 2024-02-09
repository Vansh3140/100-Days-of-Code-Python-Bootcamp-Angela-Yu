#Importing Libraries
import art
import random
import game_data
from replit import clear

continue_game=True
score=0
num1=random.randint(0,len(game_data.data)-1)
num2=random.randint(0,len(game_data.data)-1)


def followers(num1,num2):
  """
  A function to compare the Followers of Option A and B
  """
  if game_data.data[num1]['follower_count']>=game_data.data[num2]['follower_count']:
     return True
  else:
     return False

while continue_game==True:
  print(art.logo)
  if score>0:
    print(f"You are right!! Your score is {score}\n")
  
  print(f"Compare A: {game_data.data[num1]['name']}, a {game_data.data[num1]['description']}, from {game_data.data[num1]['country']}.")
  
  print(art.vs)

  print(f"Compare B: {game_data.data[num2]['name']}, a {game_data.data[num2]['description']}, from {game_data.data[num2]['country']}.\n")

  choice=input("Who has more followers? Type 'A' or 'B': ").lower()

  if followers(num1,num2)==True:
    if choice=='a':
      num2=random.randint(0,len(game_data.data)-1)
      score+=1
    else:
      continue_game=False
  else:
    if choice=='b':
      num1=num2
      num2=random.randint(0,len(game_data.data)-1)
      score+=1
    else:
      continue_game=False
  clear()

print(art.logo)
print(f"You are Wrong and your final score is {score}\n")
  