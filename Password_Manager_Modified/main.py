from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = [random.choice(letters) for x in range(nr_letters)]
password_symbol=[random.choice(symbols) for x in range(nr_symbols)]
password_number=[random.choice(numbers) for x in range(nr_numbers)]
final_list=password_list+password_symbol+password_symbol

random.shuffle(final_list)

gen_password = "".join(final_list)
pyperclip.copy(gen_password)

# print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def search_data():
    website_name = website_entry.get()
    try:
        with open("password_data.json","r") as file:
            data=json.load(file)
        email_name=data[website_name]["Email"]
        password_name=data[website_name]["Password"]
        messagebox.showinfo(title="Record Found",message=f"Email:{email_name}\nPassword:{password_name}")
    except:
        messagebox.showinfo(title="Not Found",message=f"There are no records for {website_name} company.")
    finally:
        website_entry.delete(0,END)


def get_pass():

    password_entry.insert(0,f"{gen_password}")

def add_entry():

    website_name=website_entry.get()
    email_name=email_entry.get()
    password_name=password_entry.get()
    new_data={website_name:{
        "Email":email_name,
        "Password":password_name
    }}

    if len(website_name)==0 or len(password_name)==0:
        messagebox.showwarning(title="Oops!!",message="Don't Leave these fields empty!!")
    else:
        with open("password_data.json",mode="r") as file:
            #Reading JSON
            try:
                data=json.load(file)
            #Updating JSON
                data.update(new_data)
            except:
                data=new_data
            finally:
                with open("password_data.json",mode="w") as file:
                    #Writing JSON
                    json.dump(data,file,indent=4)

        messagebox.showinfo(title="Success",message="Details Saved Successfully!! 🥳🎉")

    website_entry.delete(0,END)
    email_entry.delete(0,END)
    password_entry.delete(0,END)
    email_entry.insert(0,"chdvanshsingh@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)

#Logo

logo=Canvas(width=200,height=200)
img=PhotoImage(file="logo.png")
logo.create_image(100,100,image=img)
logo.grid(column=1,row=0)

#Label1

website=Label(text="Website:",font=("Sans-Serif",10))
website.grid(column=0,row=1)
website.config(pady=10)

#Entry1

website_entry=Entry(width=33)
website_entry.focus()
website_entry.grid(column=1,row=1)

#Search Button

search=Button(text="Search",font=("Sans-Serif",10),command=search_data,width=12)
search.grid(column=2,row=1)

#Label2

email=Label(text="Email/Username:",font=("Sans-Serif",10))
email.grid(column=0,row=2)
email.config(pady=10)

#Entry2

email_entry=Entry(width=55)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"chdvanshsingh@gmail.com")

#Label3

password=Label(text="Password:",font=("Sans-Serif",10))
password.grid(column=0,row=3)
password.config(pady=10)

#Entry3

password_entry=Entry(width=34)
password_entry.grid(column=1,row=3)

#Generate Password

gen_pass=Button(text="Generate Password",font=("Sans-Serif",10),command=get_pass)
gen_pass.grid(column=2,row=3)

#Add Buttom

add_pass=Button(text="Add",width=42,font=("Sans-Serif",10,"bold"),command=add_entry)
add_pass.grid(column=1, row=4, columnspan=2)

window.mainloop()