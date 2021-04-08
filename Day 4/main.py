rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game=[rock,paper,scissors]
import random as rand
user_input=int(input("Choose one: 0 for rock, 1 for paper, 2 for scissors:"))
print(game[user_input])
computer_input=rand.randint(0,2)
print("Computer chose: ")
print(game[computer_input])
if(user_input!=computer_input):
  if((user_input==0 and computer_input==1) or (computer_input==0 and user_input==1)):
    if(user_input==0):
      print("You Loose")
    else:
      print("You Win")
  if((user_input==1 and computer_input==2) or (computer_input==1 and user_input==2)):
    if(user_input==1):
      print("You Loose")
    else:
      print("You Win")
  if((user_input==0 and computer_input==2) or (computer_input==0 and user_input==2)):
    if(user_input==2):
      print("You Loose")
    else:
      print("You Win")
else:
  print("DRAW MATCH")
  
