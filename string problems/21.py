#Validate a password based on these conditions: 
#Minimum 8 characters 
#At least one uppercase letter 
#One lowercase letter 
#One digit 
#One special character
password = input("write password: ")
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Valid")
else:
    print("Invalid")