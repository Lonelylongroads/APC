import student

marks_list = [85, 90, 78, 92, 88]
tot = student.total_marks(marks_list)
pct = student.percentage(marks_list)
grd = student.grade(pct)

print("Total Marks:", tot)
print("Percentage:", pct)
print("Grade:", grd)