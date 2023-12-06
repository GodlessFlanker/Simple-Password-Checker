import re
import getpass
#With the getpass module, we make our pass not visible when we type it

def check_password(password):
    if len(password) < 8:
        raise Exception("Your Password must be at leats 8 digits")
    elif not re.search("[a-z]",password): 
        raise Exception("Your password should contain lowercase letter")
    elif not re.search("[A-Z]",password): 
        raise Exception("Your password should contain uppercase letter") 
    elif not re.search("[0-9]",password): 
        raise Exception("Your password should contain numbers between 0-9")
 #You can add various conditions here, it is just a simple one built with re module.
 #For example you can request the password to contain at least one special character like !,%, %,@. 
 #After this I leave it to your imagination. If you have any questions dont hasitate to contact me from my discord:
 #                                 // godless_scripts // 

while True:
    password = getpass.getpass("Enter your password: ") 
    try:
        check_password(password)
        break
    except Exception as e:
        print(e)
        print("Please try again")

print("Your password is correct")