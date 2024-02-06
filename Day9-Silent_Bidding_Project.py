from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

flag="yes"
bidders={}
print(logo)
print("Welcome to the secret auction program.")

while flag=="yes":
  name=input("What is your name?:")
  bid=int(input("What's your bid?:"))
  bidders[name]=bid
  flag=input("Are there any other bidders? Type 'yes' or 'no'.")
  clear()

maxi=-99999
max_bidder=""

for key in bidders:
  amount=bidders[key]
  if amount>maxi:
    maxi=amount
    max_bidder=key

print(f"The winner is {max_bidder} with {maxi} bid.")

