s = int(input())
for i in range(s):
    n, r = input().split()
    for j in r:
        print(j*int(n), end="")
    print()