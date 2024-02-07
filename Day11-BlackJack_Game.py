from replit import clear
import random 

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)
print("Welcome to BlackJack Game\n")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10]

flag="y"

#Function to assign random cards

def add_cards(n):
  list=[]
  for x in range(0,n):
    num=random.randint(0,12)
    list.append(cards[num])
  return list

while flag=="y":
  user_cards=add_cards(2)
  computer_cards=add_cards(2)
  print(f"Dealer has [_,{computer_cards[1]}]\n")
  print(f"You have {user_cards} with sum of {sum(user_cards)}\n")
  user_decision="hit"

  user_score=sum(user_cards)
  computer_score=sum(computer_cards)
  result=-1

  while (user_decision=="hit" and user_score<=21) or user_score<16:
    user_decision=input("Do you want to hit or stand?Type 'hit' or 'stand'\n")
    if user_decision=="stand":
      break
    else:
      user_cards.append(add_cards(1)[0])
    user_score=sum(user_cards)
    print(f"You have {user_cards} with sum of {sum(user_cards)}\n")
    
  computer_decision=random.randint(0,1)
  
  while (computer_decision==1 and computer_score<=21)or computer_score<16:
    computer_cards.append(add_cards(1)[0])
    computer_decision=random.randint(0,1)
    computer_score=sum(computer_cards)

  #0=draw ,1=user win,2=computer win

  if user_score>21:
    if computer_score>21:
      result=0
    else:
      result=2
  elif computer_score>21:
    result=1
  elif user_score>computer_score:
    result=1
  elif user_score<computer_score:
    result=2
  else:
    result=0

  print(f"Dealer has {computer_cards}\n")
  print(f"You have {user_cards}\n")
  
  if result==0:
    print("There is a draw\n")
  elif result==1:
    print("Hurray You win!!\n")
  else:
    print("Sorry You lose !!\n")

  flag=input("Do you want to continue this game?Type 'y' or 'n'\n")
  clear()