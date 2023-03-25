## *Pands* *Problem* *Sheet* :two: :zero: :two: :three:
---
I utilized this repository for completing the weekly assessments assigned during the Programming and Scipting module of the Higher Diploma in Data Analytics course offered by ATU university.
My process for arriving at the solutions to the assigned tasks is described here, including the sources I consulted and the technologies employed for coding and testing.

## **Table** **of** **Contents**
---
1. [Weekly Tasks](#WeeklyTasks)
    * [Hello World!](#HelloWorld)
    * [Bank Currency Calculator](#BankCurrencyCalculator)
    * [Bank Account Number Security](#BankAccountNumberSecurity)
    * [Collatz](#Collatz)
    * [Weekday Checker](#WeekdayChecker)
    * [Square Root](#SquareRoot)
    * [Counting 'e's in a Text File](#Counting'e'sinaTextFile)
    * [Plotting](#Plotting) 

---

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

---

###### *Weekday* *Checker* <a name="Weekday Checker"></a>

> Write a program that outputs whether or not today is a weekday. 

---


###### *Square* *Root* <a name="SquareRoot"></a>

> Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

---


###### *Counting* *'e'* *s* *in* *a* *Text* *File* <a name="Counting'e'sinaTextFile"></a>

>Write a program that reads in a text file and outputs the number of e's it contains.

---


### *Plotting* <a name="Plotting"></a>
>Write a program that displays:
>1. a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
>2. and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.

---


[^1]: As showed in Lesson: Topic 4 (Controlling the flow)
[^2]: 2.Use Unicode glyph number: https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python
[^3]: Stack Overflow was used to understand better how to mask the first 6 digits of a Bank Account number: https://stackoverflow.com/questions/9730653/is-there-a-better-way-to-mask-a-credit-card-number-in-python



