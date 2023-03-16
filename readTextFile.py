#program that reads in a text file and outputs the number of E's it contains

#Author: Francesco Troja


def letter_frequency(FILENAME, letter):
    with open(FILENAME, "r") as f:
        doc = f.read()
        return doc.count("e") #the esiest way to find the number of E in the text was to use the count() method

print(letter_frequency("text.txt", "e"))




