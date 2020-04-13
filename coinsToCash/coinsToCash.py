def calc_dollars(**coins):
    cents = coins['nickels'] * 5 + coins['pennies'] + coins['dimes'] * 10 + coins['quarters']*25
    dollars = cents / 100
    return dollars
print(calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)  )

dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

import math

def deconstruct(amount):
    leftOver = amount*100
    quarters = math.floor(leftOver / 25)
    piggyBank["quarters"] = quarters
    leftOver -= (quarters * 25)
    
    dimes = math.floor(leftOver / 10)
    piggyBank["dimes"] = dimes
    leftOver -= (dimes * 10)

    nickels = math.floor(leftOver / 5)
    leftOver -= (nickels * 5)
    piggyBank["nickels"] = nickels

    pennies = leftOver
    piggyBank["pennies"] = pennies

    print(piggyBank)

    

deconstruct(8.49)
