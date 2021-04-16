import art
import random as rand
from replit import clear

# functions
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return rand.choice(cards)

def calc_score(user_comp):
    """ Returns the score in the list using sum function """
    if sum(user_comp)==21 and len(user_comp)==2 :
        return 0
    if 11 in user_comp and sum(user_comp)>21 :
        user_comp.remove(11)
        user_comp.append(1)
    
    return sum(user_comp)

def compare(user_score,comp_score):
    if user_score==comp_score:
        return "Draw 🙄"
    elif comp_score==0:
        return "Loose, Opponent has Blackjack 😅 "
    elif user_score==0:
        return "You won, you got a Blackjack 😎"
    elif user_score>21:
        return "You went over. You Lose. 😓"
    elif comp_score>21:
        return "Opponent went over. You won. 😁"
    elif user_score>comp_score:
        return "You won. 😊"
    else:
        return "You lose. 😭"
# main code play() function
def play():
    print(art.logo)
    user=[]
    comp=[]


    for _ in range(2):
        user.append(deal_card())
        comp.append(deal_card())

    is_game_over=False

    while not is_game_over:
        user_score=calc_score(user)
        comp_score=calc_score(comp)
        print(f" Your cards: {user}, current score: {user_score} ")
        print(f" Computer's First card: {comp[0]} ")
        if user_score==0 or comp_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, else type 'n' to pass.")
            if user_should_deal=='y':
                user.append(deal_card())
            else:
                is_game_over=True

    while comp_score!=0 and comp_score<17:
        comp.append(deal_card())
        comp_score=calc_score(comp)

    print(f" Your final hand is {user} and final score is: {user_score}")
    print(f" Computer cards are: {comp} and final score is {comp_score}")
    print(compare(user_score,comp_score))



while input("Do you want to play a game of Blackjack? Type 'y' or 'n'") =="y":
    clear()
    play()


