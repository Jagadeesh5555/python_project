'''  I am checking the validation of an email'''
import re

def valid_email(email_list):
    valid_email_list=[]
    for email in email_list:
        regex='^[a-zA-Z0-9_+=.]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
        valid_email_list.append("valid" if re.match(regex,email) else "invalid")
    return valid_email_list




def main():
    n=int(input("Enter the no of emails you want to check"))
    emails=[]
    for _ in range(n):
        emails.append(input())
    return emails




email_list=main()
validation_email=valid_email(email_list)
for i in range(len(validation_email)):
        print(f" Validation: {validation_email[i]}")
