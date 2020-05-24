import re

print('''Password Validator
Checks if email and password are correctly entered

email requirements
numbers and letter + @ + letters and numbers + . letters

password requirements
Atleast 8 char long
contain letter, numbers, $%#@!*&\n\n\n''')

email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password = re.compile(r"[A-Za-z0-9$%#@!*&]{8,}")

mail = input("Enter email: ")
pswd = input("Enter passsword: ")

check_mail = email.fullmatch(mail)
check_pswd = password.fullmatch(pswd)

if check_mail:
        print("Email meets requirements.")
else:
        print("Email does not meet requirements.")
        
if check_pswd:
        print("Password meets requirements.")
else:
        print("Password does not meet requirements.")
