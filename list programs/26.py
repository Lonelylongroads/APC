#Store marks of 20 students in a list and determine:
#Highest marks
#Lowest marks
#Average marks
#Number of students scoring above average
#Number of students scoring below average


marks = [85, 72, 90, 45, 60, 88, 95, 50, 67, 73, 81, 39, 92, 58, 64, 77, 83, 49, 91, 68]

high = max(marks)
low = min(marks)
avg = sum(marks) / 20

above = sum(1 for m in marks if m > avg)
below = sum(1 for m in marks if m < avg)

print("Highest marks:", high)
print("Lowest marks:", low)
print("Average marks:", avg)
print("Students above average:", above)
print("Students below average:", below)