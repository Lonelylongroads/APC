#Validate whether a given email address follows a valid format. 
import re

email = input("write email: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern, email):
    print("Valid")
else:
    print("Invalid")