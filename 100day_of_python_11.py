############### Blackjack Project #####################
import os
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
def blackjack():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    usercard = []
    compcard = []
    usercard.append(cards[random.randint(0,12)])
    usercard.append(cards[random.randint(0,12)])
    print(f"your cards[{usercard[0]},{usercard[1]}],current score:{usercard[0]+usercard[1]}")
    compcard.append(cards[random.randint(0,12)])
    print(f"computer's first card:{compcard[0]}")
    another_card = input("Type 'y' to get another card, type 'n' to pass:")

    if another_card == 'y':
        while another_card == 'y':
            usercard.append(cards[random.randint(0,12)])
            if sum(usercard) < 22:
                print("your cards",usercard,"current score:",sum(usercard))
                print(f"computer's first card:{compcard[0]}")
                another_card = input("Type 'y' to get another card, type 'n' to pass:")
                if another_card == 'n':
                    print("your final cards",usercard,"final score:",sum(usercard))
                    while sum(compcard)<16:
                        compcard.append(cards[random.randint(0,12)])
                        if sum(compcard)>21:
                            if 11 in compcard:
                                usercard.remove(11)
                                usercard.append(1)
                        print("computer's final card:",compcard,"final score:",sum(compcard))
                        whowin(sum(usercard),sum(compcard))
                        return input("Do you want to play a game of blackjack?, Type 'y' or 'n':")
            elif sum(usercard) > 21: 
                if 11 in usercard:
                    usercard.remove(11)
                    usercard.append(1)
                    print("your cards",usercard,"current score:",sum(usercard))
                    print(f"computer's first card:{compcard[0]}") 
                    another_card = input("Type 'y' to get another card, type 'n' to pass:")
                    if another_card == 'n':
                        print("your final cards",usercard,"final score:",sum(usercard))
                        while sum(compcard)>16:
                            compcard.append(cards[random.randint(0,12)])
                            if sum(compcard>21):
                                if 11 in compcard:
                                    usercard.remove(11)
                                    usercard.append(1)
                        print("computer's final card:",compcard,"final score:",sum(compcard))
                        whowin(sum(usercard),sum(compcard))    
                        return input("Do you want to play a game of blackjack?, Type 'y' or 'n':")
                else:
                    print("your final cards",usercard,"final score:",sum(usercard))
                    while sum(compcard)<16:
                        compcard.append(cards[random.randint(0,12)])
                        if sum(compcard)>21:
                            if 11 in compcard:
                                usercard.remove(11)
                                usercard.append(1)
                    print("computer's final card:",compcard,"final score:",sum(compcard))
                    whowin(sum(usercard),sum(compcard))
                    return input("Do you want to play a game of blackjack?, Type 'y' or 'n':")
    else:
        while sum(compcard)<16:
            compcard.append(cards[random.randint(0,12)])
            if sum(compcard)>21:
                if 11 in compcard:
                    usercard.remove(11)
                    usercard.append(1)
        print("computer's final card:",compcard,"final score:",sum(compcard))
        whowin(sum(usercard),sum(compcard))
        return input("Do you want to play a game of blackjack?, Type 'y' or 'n':")

def whowin(user,comp):
    if user > 21 and comp >21:
        print("You draw !")
    elif user > 21 and comp < 21:
        print("You lose !")
    elif user < 21 and comp >21:
        print("You win !")
    elif user > comp:
        print("you win !")
    elif comp > user:
        print("you lose!")
T = input("Do you want to play a game of blackjack?, Type 'y' or 'n':")

while True:
    if T == 'y':
        T = blackjack()
    elif T =='n':
        break