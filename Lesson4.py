# Q7 2022 paper


# Write a Python program to check if an email address has been entered correctly by a box
# user.
# Your program must:
# • get the user to input an email address
# • get the user to input the email address a second time
# • output the message Match and output the email address if the email
# addresses entered are the same
# • output the message Do not match if the email addresses entered are
# not the same.
# You should use indentation as appropriate, meaningful variable name(s) and Python
# syntax in your answer.


email_address = input("enter email address: ")
email2 = input("enter email address again: ")
if email_address == email2:
    print("Match")
    print(email_address)
else:
    print("Do not match")     

 