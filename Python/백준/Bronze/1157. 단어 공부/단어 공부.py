a = input().upper()
c = set(a)
b = []

for i in c:
    b.append(a.count(i))
    
if (b.count(max(b)) > 1):
    print("?")
else:
    print(list(c)[b.index(max(b))])
