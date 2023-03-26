## *Pands* *Problem* *Sheet* :two: :zero: :two: :three:

I utilized this repository for completing the weekly assessments assigned during the Programming and Scipting module of the Higher Diploma in Data Analytics course offered by ATU university.
My process for arriving at the solutions to the assigned tasks is described here, including the sources I consulted and the technologies employed for coding and testing.

## **Table** **of** **Contents**

1. [Weekly Tasks](https://github.com/C-3sc0/pands-problem-sheet#weekly-tasks-)
    * [Hello World!](#HelloWorld)
    * [Bank Currency Calculator](#BankCurrencyCalculator)
    * [Bank Account Number Security](#BankAccountNumberSecurity)
    * [Collatz](#Collatz)
    * [Weekday Checker](#WeekdayChecker)
    * [Square Root](#SquareRoot)
    * [Counting 'e's in a Text File](#Counting'e'sinaTextFile)
    * [Plotting](#Plotting) 


# ***Weekly*** ***Tasks*** <a name="WeeklyTasks"></a>
---
## *Hello* *World* <a name="HelloWorld"></a>

> Write a program that display Hello World!

This program, when run, will show the message "Hello World!". It serves as a standard introductory program that demonstrates Python's basic syntax and utility to those new to the world of computer programming.

---

### *Bank* *Currency* *Calculator* <a name="BankCurrencyCalculator"></a>

>Write a program that asks the user to input 2 money amounts (in cents) and then calculates their sum.
>The output is presented with a € sign and decimal point separating the euro and cent values of the amount

This program is designed to perform basic currency calculations.
The program's limitation is that it does not verify or check the user's input to ensure that the inputted values are indeed legitimate money amounts. It does not, for example, verify that the input numbers are non-negative integers or that they reflect valid monetary values.
To resolve this problem, a while loop[^1] has been added to ask the user to enter a valid non-negative number after entering a negative amount. This guarantees that the program only operates on valid monetary values and returns the correct result. 

One of the challenges of this program was finding a way to output the € sign. After a research on the web I found helpful information on Stack Overflow[^2] website whch offered various opton to solve the problem. I choose to incorporate the € Unicode glyph number: 
```
\u20ac
```
into my code.

---

#### *Bank* *Account* *Number* *Security* <a name="BankAccountNumberSecurity"></a>

> Write a program that reads in a 10 character account and ouputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)
> Extra: Modify the program to deal with account numbers of any length

This program is designed to show the last 4 digits of a 10 digit bank account number, replacing the first 6 digits with an 'X'[^3]. However, the program's limitation was that it could not display the account numbers of any length, as it always showed only the last 4 digits. To overcome this limitation and fulfill the extra requirement, a different approach was adopted taking the percentages as reference.
Instead of always displaying the last 4 digits, the program now shows 40% of the total digits in the account number and replaces the remaining digits with "X" characters. For example, if the account number is "4567894561", only the first 40% (i.e., "XXXXXX4561") will be displayed. This approach enables the program to handle account numbers of any length, making it more flexible and versatile.



---

##### *Collatz* <a name="Collatz"></a>

>Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
>At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Even though the assignment did not expressly require it, a *while* *loop* was introduced to manage negative numbers that may have been entered incorrectly. 
Furthermore, a second *while* *loop* has been added to check whether a number is odd or even by using conditional statements (**if** and **else**), and continues to do so until the value reaches one. 
The *"if"* statement uses the modulus operation to determine if the number is even; if the remainder is zero, the program divides the number by two and prints it. Otherwise, the *"else"* statement multiplies the number by three and adds one, and prints the result. To make the output neater, the **'end[^4] = " " '** parameter is used to write the output in a single line.

---

###### *Weekday* *Checker* <a name="Weekday Checker"></a>

> Write a program that outputs whether or not today is a weekday. 

In order to complete the task, it was necessary to import the *datetime*[^5] module, so we could manipulate date and time.
Thanks to the documentation of geeksforgeeks, it was able to find the missing piece to crack the code.
There it was discovered that by using *date.isoweekday()*[^6], where Monday is 1 and Sunday is 7, it is simple to determine whether today is a weekday or a weekend with the aid of an if expression.

---


###### *Square* *Root* <a name="SquareRoot"></a>

> Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

Before being able to crack the code, few hours of research have been used to better understand how the "Newton's method for square roots" works. Website as [geeksforgeeks](https://www.geeksforgeeks.org/program-for-newton-raphson-method/) , [hackernoon](https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo), [tutorialsinhand](https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx#:~:text=If%20a%20given%20number%20is,correct%20square%20root%20of%20N),[runestone](https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html) & an [Youtube](https://www.youtube.com/watch?v=szQUIRPrAgQ&ab_channel=mechtutorcom) Video have been used for research purpose.
Function was created with a keyword def sqrt(n). In the function variable n is defined as the user input. 
To round the float number to 3 decimal points, the *round ()*[^7] has been used.

---


###### *Counting* *'e'* *s* *in* *a* *Text* *File* <a name="Counting'e'sinaTextFile"></a>

>Write a program that reads in a text file and outputs the number of e's it contains.

This program needs users to provide the file name as an argument in the command line in order to view a particular text file.
To ensure that the requested file is in the same directory as the program, the sys method was imported. Using the sys.argv[1] variable, it is defined that the filename is second argument when calling a program ( sys.argv[0] is the program we are trying to start).
To open the requested file for reading, the open(filename, 'r') function is used.
To count occurrences of both the lowercase letter 'e' and the uppercase letter 'E', a for loop was utilized in combination with conditional statements using "if". 

---


### *Plotting* <a name="Plotting"></a>
>Write a program that displays:
>1. a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
>2. and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.

Like the Square root tasks, prior to crack the code, I spent a few hours of study to acquire a better grasp of its mechanics. Throughout this study, I examined a variety of sources to help me understand it better.

To do the plot libraries numpy and matplotlib.pyplot had to be imported.
Normal distrbution was found using the random.normal() functon, while range for the h(x)=x3 function was found using the arange() function from numpy library.
The title, and both the x and y axis were labeled using the functions title(), xlabel() and ylabel() respectively from the matplotlib.pyplot library.
The output of this task for the user is a saved image of the plot in the same directory (folder) as the program creating the plot.

---


[^1]: As showed in Lesson: Topic 4 (Controlling the flow)
[^2]: 2.Use Unicode glyph number: [StackOverflow](https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python)
[^3]: [StackOverflow](https://stackoverflow.com/questions/9730653/is-there-a-better-way-to-mask-a-credit-card-number-in-python) was used to understand better how to mask the first 6 digits of a Bank Account number. 
[^4]: [geeksforgeeks](https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/) helps in understand better ho to use the 'end = " "' parameter. 
[^5]: [w3schools](https://www.w3schools.com/python/python_datetime.asp) helps in research and understand how to implement the datetime module.
[^6]: [geeksforgeeks](https://www.geeksforgeeks.org/isoweekday-method-of-datetime-class-in-python/)
[^7]: [Pythonhow](https://pythonhow.com/how/limit-floats-to-two-decimal-points/#:~:text=To%20limit%20a%20float%20to,resulting%20in%20the%20value%203.14)



