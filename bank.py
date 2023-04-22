#Program should prompt the user and read in two money amounts (in cents).
#Print out the answer with Euro sign and decimal point beteen the euro and cent of the amount

#Author: Francesco Troja

# define a function called bank
def bank():
    # prompt the user to enter the first amount
    while True:
        try:
            amount = int(input("Enter amount1: "))
# Check if the amount is negative and ask the user to enter a positive amount if it is
            if amount < 0:
                print("Invalid amount entered. Please enter a positive amount.")
# skip to the next iteration of the while loop when the user enters an invalid amount                
                continue
# break out of the loop if the input is valid
            break
# print an error message if the user enters a non-integer value
        except ValueError:
            print("Invalid amount entered. Please enter a positive integer.")
    # prompt the user to enter the second amount
    while True:
        try:
            amount1 = int(input("Enter amount2: "))
            if amount1 < 0:
                print("Invalid amount entered. Please enter a positive amount.")
                continue
            break
        except ValueError:
            print("Invalid amount entered. Please enter a positive integer.")
    total = amount + amount1
    return total

sum = bank()
#get the total number of euros
euro= sum // 100
#get the number of cents remaining.
cent = sum % 100
# print the sum with a Euro symbol using Unicode (code point U+20AC)
print(f'The sum of these is \u20ac{euro}.{cent:02d}') #:02d to always includes the 2 decimal places expeced fro a currency amount.
