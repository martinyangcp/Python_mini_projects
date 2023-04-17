logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
    code=[]
    shift %= 26
    if direction =='encode':
        text = list(text)
        for ii in range(len(text)):
            for i in range(len(alphabet)):
                if text[ii] == alphabet[i]:
                    code.append(i+shift)
        for i in range(len(code)):
            if code[i] >= 26:
                code[i] -=26
            code[i] = alphabet[code[i]]
        code = ''.join(code)
        print(f"encoded text is {code}")
    elif direction == 'decode':
        text = list(text)
        for ii in range(len(text)):
            for i in range(len(alphabet)):
                if text[ii] == alphabet[i]:
                    code.append(i-shift)
        for i in range(len(code)):
            if code[i] < 0:
                code[i] +=26
            code[i] = alphabet[code[i]]
        code = ''.join(code)
        print(f"The decoded text is {code}")
        

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text,shift,direction)
    again = input("Do you want to restart the cipher program?")
    if again =='yes':
        pass
    elif again =='no':
        print("Bye")
        break