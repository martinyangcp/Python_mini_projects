logo = '''
___________                        _________                      __  .__    .__                 
\__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____   
  |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\  
  |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  > 
  |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /  
          \/     |__|        \/          \/             \/     \/          \/        \//_____/   
'''
 
import random
def guess(g):
  
  if g > number:
    print("Too high")
    print("Guess again")
  elif g < number:
    print("Too low")
    print("Guess again")
  elif g == number:
    print("you got it! The answer was",number)
    return 'stop'

number = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

if difficulty == 'easy':
  i = 10
  while i >0:
    print(f"you have {i} attempts remaining to guess the number.")
    if guess(int(input("Make a guess:"))) == 'stop':
      break
    i -= 1
elif difficulty == 'hard':
  i = 5
  while i >0:
    print(f"you have {i} attempts remaining to guess the number.")
    if guess(int(input("Make a guess:"))) == 'stop':
      break
    i -= 1

if i == 0:
  print("you've run out of guesses, you lose.")