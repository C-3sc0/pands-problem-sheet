# *Pands* *Problem* *Sheet* - :two: :zero: :two: :three: -

I utilized this repository for completing the weekly assessments assigned during the Programming and Scipting module of the Higher Diploma in Data Analytics course offered by ATU university.
My process for arriving at the solutions to the assigned tasks is described here, including the sources I consulted for coding and testing.

## **Table** **of** **Contents**

1. [Weekly Tasks:](https://github.com/C-3sc0/pands-problem-sheet#weekly-tasks-)
    * [Hello World!](https://github.com/C-3sc0/pands-problem-sheet#hello-world-) :earth_africa:
    * [Bank Currency Calculator](https://github.com/C-3sc0/pands-problem-sheet#bank-currency-calculator-) :bank:
    * [Bank Account Number Security](https://github.com/C-3sc0/pands-problem-sheet#bank-account-number-security-) :credit_card:
    * [Collatz](https://github.com/C-3sc0/pands-problem-sheet#collatz-) :1234:
    * [Weekday Checker](https://github.com/C-3sc0/pands-problem-sheet#weekday-checker-) :calendar:
    * [Square Root](https://github.com/C-3sc0/pands-problem-sheet#square-root-)
    * [Counting 'e's in a Text File](https://github.com/C-3sc0/pands-problem-sheet#counting-e-s-in-a-text-file-) :page_facing_up:
    * [Plotting](https://github.com/C-3sc0/pands-problem-sheet#plotting-):chart_with_upwards_trend:

## ***Weekly*** ***Tasks***

-------

## *Hello* *World*

> Write a program, called **helloworld.py**, that display `Hello World!`

This program, when run, will show the message `"Hello World!"`. It serves as a standard introductory program that demonstrates Python's basic syntax and utility to those new to the world of computer programming.

<details>
<summary>Output</summary>

```python
   Hello World
```

</details>

## *Bank* *Currency* *Calculator*

>Write a program, called **bank.py**, that asks the user to input 2 money amounts (in cents) and then calculates their sum.
>The output is presented with a € sign and decimal point separating the euro and cent values of the amount

This program is designed to perform basic currency calculations.
The program defines a function called `bank()` that calculates the total of two amounts inputted by the users and returs their result in cents.
The program's limitation is that it does not verify or check the user's input to ensure that the inputted values are indeed legitimate money amounts. It does not, for example, verify if the input numbers are non-negative integers or floating numbers.
To resolve this problem, a `while loop`[^1] has been added. If the inputted amount is negative, the function prints an error message and skips to the next iteration of the while loop using the `continue` statement. Otherwise, it `breaks out` of the loop and prompts the user to enter the second amount in a similar way.

<details>
<summary>Negative Number Input</summary>

```python
Enter amount1: -45
Invalid amount entered. Please enter a positive amount.
Enter amount1:  45
```

</details>

Furthermore, a `Try` and `Excpet` block has been added to handle cases where the user inputs a non-integer value, such as a floating number, and raise a `ValueError` exception with a custom error message.
<details>
<summary>Non Integer Input</summary>

```python
Enter amount1: Hello world
Invalid amount entered. Please enter a positive amount.
Enter amount1:  78.5
Invalid amount entered. Please enter a positive amount.
Enter amount1:  78
```

</details>

One of the challenges of this program was finding a way to output the *€* *sign*. After a research on the web I found helpful information on **Stack** **Overflow**[^2] website whch offered various opton to solve the problem. I choose to incorporate the € Unicode glyph number into my code.
<details>
<summary>€ symbol</summary>

```python
\u20ac
```

</details>

### *Bank* *Account* *Number* *Security*

> Write a program, called **accounts.py**, that reads in a 10 character account and ouputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)
> Extra: Modify the program to deal with account numbers of any length

This program is designed to show the last `4 digits` of a 10 digit bank account number, replacing the first 6 digits with an `'X'`[^3]. However, the program's limitation was that it could not display the account numbers of any length, as it always showed only the last 4 digits. To overcome this limitation and fulfill the extra requirement, a different approach was adopted taking the percentages as reference.
Instead of always displaying the last 4 digits, the program now shows `40%` of the total digits in the account number and replaces the remaining digits (the remaining `60%`) with `"X"` characters. For example, if the account number is `"4567894561"`, only the first 40% (i.e., `"XXXXXX4561"`) will be displayed. This approach enables the program to handle account numbers of any length, making it more flexible and versatile.
<details>
<summary>Input</summary>

```python
Please enter an account number (any length): 7894567852
Please enter an account number (any length): 986532748659864531
```

Output

```python
XXXXXX7852
XXXXXXXXXXX9864531
````

</details>

### *Collatz*

>Write a program, called **collatz.py**, that asks the user to input any positive integer and outputs the successive values of the following calculation.
>At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Even though the assignment did not expressly require it, a `while loop` was introduced to manage `negative numbers` that may have been entered incorrectly.
<details>
<summary> Negative number input </summary>

```python
Please enter a positive integer: -78
Error! -78 is a Negative Number
Try to add a ositive iteger: -56
Error! -56 is a Negative Number
Try to add a ositive iteger: 45
```

</details>

Furthermore, a second `while loop` has been added to check whether a number is odd or even by using conditional statements (`if` and `else`), and continues to do so until the value reaches one.
The `"if"` statement uses the modulus operation to determine if the number is *even*; if the remainder is zero, the program divides the number by two and prints it. Otherwise, the `"else"` statement multiplies the number by three and adds one, and prints the result. To make the output neater, the `end= " "`parameter[^4] is used to write the output in a single line.

### *Weekday* *Checker*

> Write a program, called **weekday.py**, that outputs whether or not today is a weekday.

In order to complete the task, it was necessary to import the `datetime`[^5] module, so we could manipulate date and time.
Thanks to the documentation of **geeksforgeeks**, it was able to find the missing piece to crack the code.
There it was discovered that by using `date.isoweekday()`[^6], where *Monday* is *1* and **Sunday** is **7**, it is simple to determine whether today is a weekday or a weekend with the aid of an if expression.

### *Square* *Root*

> Write a program, called **squareroot.py**, that takes a positive floating-point number as input and outputs an approximation of its square root.

Before being able to crack the code, few hours of research have been used to better understand how the "Newton's method for square roots" works. Website as [geeksforgeeks](https://www.geeksforgeeks.org/program-for-newton-raphson-method/), [hackernoon](https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo), [tutorialsinhand](https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx#:~:text=If%20a%20given%20number%20is,correct%20square%20root%20of%20N),[runestone](https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html) & an [Youtube](https://www.youtube.com/watch?v=szQUIRPrAgQ&ab_channel=mechtutorcom) Video have been used for research purpose.

As an extra, using the conditional statement `if`, I included a check to ensure that the user's input is a positive floating-point number. If the user input is negative, the number is converted to a positive value using the `abs()` function.
<details>
<summary>Input</summary>

```python
Please enter a positive floating-point number: -89
Perhaps you meant 89.0
```

Output

```python
the square root of 89.0 is approx. 9.434
````

</details>

Function was created with a keyword `def sqrt(number)`. In the function variable *number* is defined as the user input, while *guess* is defined as an initial guess for the square root.
Next, `while loop` is checking the conditions of convergence. When conditions are no longer true, function returns the value of variable x.
To round the float number to 3 decimal points, the `round ()`[^7] has been used.

### *Counting* *'e'* *s* *in* *a* *Text* *File*

>Write a program, called **readTextFile.py**, that reads in a text file and outputs the number of e it contains.

This program needs users to provide the file name as an argument in the command line in order to view a particular text file.
To ensure that the requested file is in the same directory as the program, the *sys* *method* was imported. Using the `sys.argv[1]` variable, it is defined that the filename is second argument when calling a program (`sys.argv[0]` is the program we are trying to start).
To open the requested file for reading, the `open(filename, 'r')` function is used.
To count occurrences of both the lowercase letter 'e' and the uppercase letter 'E', a `for` `loop` was utilized in combination with conditional statements `if`.

### *Plotting*

>Write a program, called **plottask.py**, that displays:
>
>1. a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2,
>2. and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.

The code uses two differents libraries, `numpy`[^8] & `matplotlib.pyplot`[^9] to create a plot.
First, the code imports the two libraries using the `import` statement.
<details>
<summary>Libraries</summary>

```python
import numpy as np
import matplotlib.pyplot as plt
```

</details>

The Normal distrbution can be found using the *random.normal()* functon[^10], while range for the *h(x)=x3* function the*arange()* function from numpy library[^11] can be used.
The title, and both the x and y axis were labeled using the functions *title()*, *xlabel()* and *ylabel()* respectively from the matplotlib.pyplot library.
The program then creates the plot using the hist() function to plot the normal distribution and the plot() function to plot the function h(x)=x3.
The final step of the program saves the plot as an image file using the savefig() function and the file is saved in the same directory as the program that created it. The output of the program is an image of the plot for the user to view.

[^1]: As showed in Lesson: Topic 4 (Controlling the flow)
[^2]: 2.Use Unicode glyph number: [StackOverflow](https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python)
[^3]: is there a better way to mask a credit card number in python [StackOverflow](https://stackoverflow.com/questions/9730653/is-there-a-better-way-to-mask-a-credit-card-number-in-python) was used to understand better how to mask the first 6 digits of a Bank Account number.
[^7]: Limit floats to two decimal point [Pythonhow](https://pythonhow.com/how/limit-floats-to-two-decimal-points/#:~:text=To%20limit%20a%20float%20to,resulting%20in%20the%20value%203.14)
[^8]: [numpy](https://numpy.org/)
[^9]: Matplotlib pyplot [W3schools](https://www.w3schools.com/python/matplotlib_pyplot.asp)
[^10]:How to lot normal distribution over histogram in python [geeksforgeeks](https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/)
[^11]:Numpy arrange [Numpy](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)
