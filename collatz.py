#inpt a positive int ad output the following:
#if the value is even, divide it by two
#if the value is odd, multiply it by 3 and add 1

#Author: Franesco Troja

value = int(input("Please enter a positive integer: "))


while value != 1:
    if (value % 2) == 0:
            value = value // 2
            print(value, end= " ") #adding end prameter in order to avoid the creation of a new line between the different int
    else:
        (value % 2) != 0
        value = (value * 3 + 1)
        print(value, end= " ")

