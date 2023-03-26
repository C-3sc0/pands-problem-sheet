#input a positive floating-numb and output approximation of its square root.

#Author: Francesco Troja



number = float(input('"Please enter a positive floating-point number: '))

if number < 0:
    number = abs(number)
    print (f"Perhaps you meant {number}")


def sqrt(number):
    #k is the number tht we want to root.
    #guess represents an initial guess for the square root.
    k = number
    guess = k / 2.0
    #0.001 is the tolerance level for the approximation.
    while abs(guess * guess - k) >= 0.001:
        #the function updates the value of guess using the Newton-Raphson formula.
        guess = guess - (guess ** 2 - k) / (2 * guess)
    return guess


sqrt(number)
print (f"the square root of {number} is approx. {round(sqrt(number),3)}")
