
import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def calc(A,B,O):
    if O == '+':
        return A+B
    elif O == '-':
        return A-B
    elif O == '*':
        return A*B
    elif O == '/':    
        return A/B
print(logo)
A = int(input("What's the first letter?"))
print("+\n-\n*\n/\n")
O = input("pick an operation")
B = int(input("What's the second letter?"))
result = calc(A,B,O)
print(A,O,B,"=",result)
Re = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")

while True:
    if Re =='y':
        print(logo)
        A = result
        print("+\n-\n*\n/\n")
        O = input("pick an operation")
        B = int(input("What's the second letter?"))
        result = calc(A,B,O)
        print(A,O,B,"=",result)
        Re = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
    else :
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        A = int(input("What's the first letter?"))
        print("+\n-\n*\n/\n")
        O = input("pick an operation")
        B = int(input("What's the second letter?"))
        result = calc(A,B,O)
        print(A,O,B,"=",result)
        Re = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")