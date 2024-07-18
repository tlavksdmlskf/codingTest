account = list(map(int,input().split()))
price = int(input())*2

if sum(account) >= price:
    print(sum(account)-price)
else:
    print(sum(account))