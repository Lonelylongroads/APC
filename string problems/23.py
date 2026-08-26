#Compress repeated characters and return the original string if compression does not reduce the length. 
s = input("write any sentence: ")
if not s:
    print("")
else:
    res = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res += s[i - 1] + str(count)
            count = 1
    res += s[-1] + str(count)
    print(res if len(res) < len(s) else s)