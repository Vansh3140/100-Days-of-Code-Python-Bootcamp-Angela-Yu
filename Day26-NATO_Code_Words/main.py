import pandas as pd

data=pd.read_csv("nato_phonetic_alphabet.csv")

data_dict={row.letter:row.code for (index,row) in data.iterrows()}

code_name=input("Enter a name to convert in NATO Code: \n").upper()

code_name_list=[data_dict[x] for x in code_name]

print("\nHere is your code word!! ")
print(code_name_list)

