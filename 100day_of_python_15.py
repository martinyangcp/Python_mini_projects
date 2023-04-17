MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}
def report():
  print("Water:",resources["water"],"ml")
  print("Milk:",resources["milk"],"ml")
  print("Coffee:",resources["coffee"],"g")
  print("Money:","$",resources["money"])
def coffee(ans):
  if MENU[ans]["ingredients"]["water"]> resources["water"]:
    print("Sorry, there is not enough water")
  elif MENU[ans]["ingredients"]["coffee"]> resources["coffee"]:
    print("Sorry, there is not enough coffee")
  elif MENU[ans]["ingredients"]["milk"]> resources["milk"]:
    print("Sorry, there is not enough milk")
  else:
    moneycnt(ans)
def moneycnt(ans):
  quarters = float(input("how many quarters?:"))
  dimes = float(input("how many dimes?:"))
  nickles = float(input("how many nickles?:"))
  pennies = float(input("how many pennies?:"))
  total_money = quarters*0.25 + dimes*0.1 + nickles *0.05 + pennies*0.01
  if total_money < MENU[ans]["cost"]:
    print("sorry,that's not enough money. Money refunded.")
  else:  
    print("Here is $",total_money-MENU[ans]["cost"],"in change")
    print("Here is your",ans,"☕Enjoy!")

while True:
  ans =input("“What would you like? (espresso/latte/cappuccino):”")
  if ans == "report":
    report()
  elif ans == "off":
    break
  else:
    coffee(ans)
    if ans == "espresso":
      resources["money"] += 1.5
      resources["water"] -= 50
      resources["coffee"] -= 18

    elif ans == "latte":
      resources["money"] += 2.5
      resources["water"] -= 200
      resources["coffee"] -= 24
      resources["milk"] -= 150

    elif ans =="cappuccino":
      resources["money"] += 3.0
      resources["water"] -= 250
      resources["coffee"] -= 24
      resources["milk"] -= 100