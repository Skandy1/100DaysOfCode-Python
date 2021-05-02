import pandas
f1=pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
nato_dict={row.letter:row.code for (index,row) in f1.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input=input("Enter your name: ").upper()
list_nato=[]
for x in user_input:
    list_nato.append(nato_dict[x])
print(list_nato)
