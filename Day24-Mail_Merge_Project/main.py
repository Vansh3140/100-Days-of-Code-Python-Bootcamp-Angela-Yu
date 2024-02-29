with open("./input/Names/invited_names.txt",mode="r") as file:
    names=file.readlines()

for x in range(0,len(names)):
    names[x]=names[x].strip("\n")
    # print(names[x])

main_file=open("./input/Letters/starting_letter.txt",mode="r")
contents=main_file.read()
main_file.close()

for x in range(0,len(names)):
    if x==0:
        contents=contents.replace("[name]",names[x])
    else:
        contents=contents.replace(names[x-1],names[x])
    # print(contents)
    with open(f"./Output/ReadyToSend/letter_for_{names[x]}.txt",mode="w") as file:
        file.write(contents)