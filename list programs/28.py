#Store scores of a batsman in 10 matches and calculate:
#Highest score
#Lowest score
#Total runs
#Average runs
#Number of centuries(≥100)
#Number of half-centuries (50– 99)


score = [102, 45, 67, 89, 12, 134, 55, 0, 78, 92]

high = max(score)
low = min(score)
total = sum(score)
avg = total / len(score)

century = sum(1 for s in score if s >= 100)
half = sum(1 for s in score if 50 <= s <= 99)

print("Highest score:", high)
print("Lowest score:", low)
print("Total runs:", total)
print("Average runs:", avg)
print("Centuries:", century)
print("Half-centuries:", half)