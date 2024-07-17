cal = list(map(int,input().split()))

if (sum(cal) >= 100):
    print("OK")
else:
    if (cal.index(min(cal)) == 0):
        print("Soongsil")
    elif(cal.index(min(cal)) == 1):
        print("Korea")
    elif(cal.index(min(cal)) == 2):
        print("Hanyang")