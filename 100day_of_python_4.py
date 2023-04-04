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

#Write your code below this line 👇

import random 



while True:
    cho = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    ccho = random.randint(0,2)
    print(ccho)
    if cho == 0:
        if ccho == 0:
            print(rock)
            print("Computer chose:")
            print(rock)
            print("Draw")
        elif ccho == 1:
            print(rock)
            print("Computer chose:")
            print(paper)
            print("You lose")
        else:
            print(rock)
            print("Computer chose:")
            print(scissors)
            print("You win")
    if cho == 1:
        if ccho == 0:
            print(paper)
            print("Computer chose:")
            print(rock)
            print("You win")
        elif ccho == 1:
            print(paper)
            print("Computer chose:")
            print(paper)
            print("Draw")
        else:
            print(paper)
            print("Computer chose:")
            print(scissors)
            print("You lose")
    if cho == 2:
        if ccho == 2:
            print(scissors)
            print("Computer chose:")
            print(rock)
            print("You lose")
        elif ccho == 1:
            print(scissors)
            print("Computer chose:")
            print(paper)
            print("You Win")
        else:
            print(scissors)
            print("Computer chose:")
            print(scissors)
            print("Draw")