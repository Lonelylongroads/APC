#Store the temperature of 30 days and determine: 
#Hottest day 
#Coldest day 
#Average temperature 
#Days above average temperature 
#Days below average temperature

temp = [30, 32, 31, 29, 28, 35, 36, 33, 31, 30, 27, 26, 34, 38, 37, 32, 30, 29, 31, 33, 35, 34, 28, 27, 29, 32, 31, 30, 36, 33]

hot = max(temp)
cold = min(temp)
avg = sum(temp) / len(temp)

above = sum(1 for t in temp if t > avg)
below = sum(1 for t in temp if t < avg)

print("Hottest day temp:", hot)
print("Coldest day temp:", cold)
print("Average temperature:", avg)
print("Days above average:", above)
print("Days below average:", below)