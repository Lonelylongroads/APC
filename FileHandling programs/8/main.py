# main.py
from student import marks, grade, attendance

m = [85, 90, 80]
tot = marks.total(m)
pct = marks.percentage(m)

print("Total:", tot)
print("Percentage:", pct)
print("Grade:", grade.calculate_grade(pct))
print("Eligible:", attendance.check_eligibility(78))