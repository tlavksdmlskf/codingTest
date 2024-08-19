print("Gnomes:")
for _ in range(int(input())):
    a = list(map(int,input().split()))

    if (a == sorted(a) or a == sorted(a, reverse = True)):
        print("Ordered")
    else:
        print("Unordered")