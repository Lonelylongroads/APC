def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(pct):
    if pct >= 90:
        return 'A'
    elif pct >= 75:
        return 'B'
    elif pct >= 60:
        return 'C'
    elif pct >= 40:
        return 'D'
    else:
        return 'F'