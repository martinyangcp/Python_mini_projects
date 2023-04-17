print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? #"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
money = total_bill*(100+percentage)/100/people
print(f"Each person should pay:{round(money,2)}")