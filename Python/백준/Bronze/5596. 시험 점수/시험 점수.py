score1 = sum(map(int,input().split()))
score2 = sum(list(map(int,input().split())))

if score1 >= score2:
    print(score1)
else:
    print(score2)