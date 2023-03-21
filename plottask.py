# Write a program that displays:
#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
#and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.

#Author = Francesco Troja

import numpy as np
import matplotlib.pyplot as plt

mean = 5
standard_deviation = 2
value = np.random.normal (mean,standard_deviation, 1000)

x = np.arange (0, 10, 1)
h = x**3

font = {"family" : "papyrus", "color" : "Black", "size" : 15}

plt.hist(value, color = "lightblue", ec = "Black", lw=2)
plt.plot(h, marker = "D", ms = 5 , color = "Black", mfc="r", linestyle = "dashed", linewidth = "2.5")
plt.title("Plottask.py", fontdict = font)
plt.xlabel("Function", fontdict = font)
plt.ylabel("X Value", fontdict = font)
plt.grid(linewidth = 0.2)
plt.legend(["h(x)=x3", "Normal Distribution"], loc="upper left")
plt.savefig("Normal Distribution.png")

