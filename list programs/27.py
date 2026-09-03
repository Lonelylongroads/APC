#Store salaries of employees and determine:
#highest salary
#Lowest salary
#Average salary
#Employees earning above ₹ 50,000
#Employees earning below ₹ 30,000
salary = [45000, 60000, 25000, 80000, 28000, 52000, 35000, 90000, 22000, 55000]

high = max(salary)
low = min(salary)
avg = sum(salary) / len(salary)

above = [s for s in salary if s > 50000]
below = [s for s in salary if s < 30000]

print("Highest salary:", high)
print("Lowest salary:", low)
print("Average salary:", avg)
print("Employees earning above 50,000:", above)
print("Employees earning below 30,000:", below)