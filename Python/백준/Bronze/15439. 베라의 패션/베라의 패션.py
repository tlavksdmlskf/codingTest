n = int(input())
s = 0
for i in range(n):
    for j in range(n):
        if i != j:
            s+=1
print(s)