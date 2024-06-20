string = input()
cnt = [0 for i in range(26)]
for i in string:
    cnt[ord(i)-ord('a')]+=1
print(*cnt)
