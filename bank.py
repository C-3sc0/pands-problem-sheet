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
    # calculate the total of the two amounts, divide by 100 (since we are using cents), and return the result
    total = (amount + amount1) / 100 
    return total

# call the bank function and store the result in a variable called sum
sum = bank()
# print the sum with a Euro symbol using Unicode (code point U+20AC)
print(f'The sum of these is \u20ac{sum}')
