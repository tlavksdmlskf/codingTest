a = []
for i in range(4):
    a.append(int(input()))

print(sum(a)//60, sum(a)%60, sep="\n")