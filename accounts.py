#program that reads in a 10 character account number
#and outputs the account nmber with only the last 4 digit showing.
#Author: Francesco Troja


#basic code that will Only show the last 4 digits of numbers of any length
bank_account = input("Please enter an 10 digit account number: ")
account_length = len(bank_account)

number_to_hide = account_length - 4
number_to_keep = bank_account[number_to_hide:]
print("X" * number_to_hide + number_to_keep)



#extra: will always show the 40% of numbers of any length
#to implement the extra exercise i thought that the easiest way was to divide the number into 2: the part that i want to show: will always be the 40% of the number & 
#the part that i want to hide will always be 60% of the number 
bank_account_1 = input("Please enter an account number (any length): ")
account_length_1 = len(bank_account_1)
len_show = int(account_length_1 * 0.40)
len_hide = account_length_1 - len_show
len_to_keep = bank_account_1 [len_hide:]
print("X" * len_hide + len_to_keep)




