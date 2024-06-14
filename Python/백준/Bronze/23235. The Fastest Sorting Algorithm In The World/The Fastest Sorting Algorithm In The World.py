count = 1
while True:
    num = list(map(int,input().split()))

    if num[0] == 0:
        break
    else:
        print(f"Case {count}: Sorting... done!")
        count+=1
