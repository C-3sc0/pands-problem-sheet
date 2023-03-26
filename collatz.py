#inpt a positive int ad output the following: if the value is even, divide it by two if the value is odd, multiply it by 3 and add 1

#Author: Franesco Troja


def collatz(value):
    while value <= 0:
        print(f"Error! {value} is a Negative Number")
        value = int(input("Try to add a positive integer: "))

    while value != 1:
        print(value, end= " ")
        if (value % 2) == 0:
            value = value // 2
        else:
            value = (value * 3 + 1)
    else:
        print(value, end= " ") #adding end prameter in order to avoid the creation of a new line between the different int



value = int(input("Please enter a positive integer: "))
collatz(value)

