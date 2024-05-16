h, m = map(int,input().split())
delay = int(input())

if m + delay >= 60:
    print(h + (m + delay)//60 if h + (m +delay)//60 < 24 else (h + (m + delay)//60) - 24, (m + delay)%60)
else:
    print(h, m + delay)