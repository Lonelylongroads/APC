#Rotate a list: 
#Left by one position 
#Right by one position


num = [1, 2, 3, 4, 5]

l = num[1:] + num[:1]
r = num[-1:] + num[:-1]

print("Left rotated by 1:", l)
print("Right rotated by 1:", r)