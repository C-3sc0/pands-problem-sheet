#input a positive floating-numb and output approximation of its square root.

#Author: Francesco Troja


#https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html
def sqrt(n):
    approx = 0.5 * n
    better = 0.5 *(approx + n/approx)
    while better != approx:
        approx = better
        better = 0.5 *(approx + n/approx)
    return approx


n = float(input("Please enter a positive number: "))
print (f"the square root of {n} is approx. {round(sqrt(n),1)}") #per round() https://pythonhow.com/how/limit-floats-to-two-decimal-points/#:~:text=To%20limit%20a%20float%20to,resulting%20in%20the%20value%203.14.
