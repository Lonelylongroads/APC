#Create a list of cities. Ask the user to enter a city name and check whether it exists in the list

cities = ["Mumbai", "Delhi", "Bangalore", "Pune", "Hyderabad"]

n = input("Enter a city name: ")

if n in cities:
    print("Exists!")
else:
    print("Does not exist...")