import datetime as dt
import pandas as pd
import smtplib
import random

today=dt.datetime.now()
info=None
data=pd.read_csv("birthdays.csv")

for (index,row) in data.iterrows():
    if row.day==today.day and row.month==today.month:
        info=row
        break

letter_num=random.randint(1,3)

with open(f"letter_{letter_num}.txt") as letter:
    content=letter.read()
    content=content.replace("[NAME]",info["name"])

username="chsingh@gmail.com"
password="acha zyada password dekhega"

with smtplib.SMTP("smtp.gmail.com",587) as connection:

    connection.starttls()
    connection.login(user=username,password=password)
    connection.sendmail(username,info["email"],msg=f"Subject:Happy Birthday {info["name"]}\n\n{content}")




