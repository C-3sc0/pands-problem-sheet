#program that reads in a 10 character account number and outputs the account nmber with only the last 4 digit showing.
#Extra: Modify the program to deal with account numbers of any length

#Author: Francesco Troja


#extra: will always show the 40% of numbers of any length
#to implement the extra exercise i thought that the easiest way was to divide the number into 2: the part that i want to show: will always be the 40% of the number & 
#the part that i want to hide will always be 60% of the number 
bank_account_1 = input("Please enter an account number (any length): ")
# Determine the lenght of the account number.
account_length_1 = len(bank_account_1)
# Determine the number of characters to show (40% of the lenght)
len_show = int(account_length_1 * 0.40)
# # Determine the number of characters to hide (60% of the lenght's remainder)
len_hide = account_length_1 - len_show
len_to_keep = bank_account_1 [len_hide:]
print("X" * len_hide + len_to_keep)




