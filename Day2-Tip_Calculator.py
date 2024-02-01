#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill?"))
total_people=float(input("How many members were there?"))
tip=float(input("How much tip do you want to give?"))
answer=round(((1+tip/100)*total_bill)/total_people,2)
print(f"Each person has to give {answer} amount.")