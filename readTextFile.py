#program that reads in a text file and outputs the number of E's it contains

#Author: Francesco Troja


import sys #the sys module is used by the user to pass a command-line arguments in the script

if len(sys.argv) < 2: 
    print("Error, please add a <filepath>")
    sys.exit(1)

filepath = sys.argv[1] #we use sys.argv[1] as sys.argv[0] will always give us the name of the script.

with open(filepath, "r") as f:
    text = f.read()

count = 0
for char in text:
    if char == "e" or char == "E":
        count += 1
#in the previous script I took into consideration to count only the lowercase 'e'. To give more accuracy i added also the chance to count the upper case 'E'.

print(count)




