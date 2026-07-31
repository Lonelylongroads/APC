#Python program to determine whether the driver is insured or not
#cases: check if driver is married then insured ; if unmarried, male and above 30 years then insurance allowed;  if unmarried, female and above 25 years then insurance allowed; else not insured


marry = str(input("Is Driver Married? (yes/no): "))

if marry == "yes":
    print("The driver is insured.")
elif marry == "no":
    gender = str(input("Enter gender (male/female): "))
    age = int(input("Enter age: "))
    
    if gender == "male" and age > 30:
        print("The driver is insured.")
    elif gender == "female" and age > 25:
        print("The driver is insured.")
    else:
        print("The driver is not insured.")
else:
    print("The driver is not insured.")