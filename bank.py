#Program should prompt the user and read in two money amounts (in cents).
#Print out the answer with Euro sign and decimal point beteen the euro and cent of the amount

#Author: Francesco Troja

def bank():
    amount = int(input("Enter amount1: "))
    amount1 = int(input("Enter amount2: "))
    total = (amount + amount1)/100 
    return total

sum = bank()
#to retrieve the € symbol, I used its Unicode glyph number
print (f'The sum of these is \u20ac{sum}')