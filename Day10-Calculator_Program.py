from replit import clear

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)
print("Welcome to the Calculator App:\n")

flag="2"
prev=-1

def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b

while flag=="1" or flag=="2":
  num1=-1
  if flag=="2":
    num1=int(input("Enter the number:\n"))
    prev=-1
  if flag=="1":
    num1=prev
  operation=input("Enter the operation you want to perform (+,-,*,/):\n")
  num2=int(input("Enter the number:\n"))
  if operation=="+":
    prev=add(num1,num2)
  elif operation=="-":
    prev=subtract(num1,num2)
  elif operation=="*":
    prev=multiply(num1,num2)
  elif operation=="/":
    prev=divide(num1,num2)
  else:
    print("Invalid operation!! \n")
  print(f"The operation of {num1} {operation} {num2} is {prev}\n")
  flag=input("Enter 1 to continue with the previous result or 2 to start a new  calculation or any other key to exit the program\n")
  clear()