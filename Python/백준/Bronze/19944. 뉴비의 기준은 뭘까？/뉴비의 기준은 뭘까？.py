s = list(map(int,input().split()))
if ((s[1] == 1 or s[1] == 2)):
    print("NEWBIE!")
elif (s[0] >= s[1]):
    print("OLDBIE!")
else:
    print("TLE!")