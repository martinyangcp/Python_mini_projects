logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os
clear = lambda: os.system('cls')
bidder= {}
other = 'yes'
maxnum = 0
print(logo)
print("welcome to the secret auction program.")

while other == 'yes':
    name = input("What is your name?:")
    bid = int(input("What's your bid?"))
    bidder[name] = bid
    other = input("Are there any other bidders? Type 'yes' or 'no'.")
    clear()
reversed_dict = dict(map(reversed,bidder.items()))
maxnum = max(reversed_dict)
print("THe winner is",reversed_dict[maxnum],"with a bid of $",maxnum)