dice = sorted(list(map(int,input().split())))

if dice.count(dice[0]) == 3:
    print(10000 + dice[1] * 1000)
elif dice[0] == dice[1] != dice[2] or dice[0] == dice[2] != dice[1]:
    print(1000+dice[0]*100)
elif dice[1] == dice[0] != dice[2] or dice[1] == dice[2] != dice[0]:
    print(1000+dice[1]*100)
elif dice[2] == dice[0] != dice[1] or dice[2] == dice[1] != dice[0]:
    print(1000+dice[2]*100)
else:
    print(max(dice)*100)