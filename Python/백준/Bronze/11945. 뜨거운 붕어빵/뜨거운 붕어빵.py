leng = list(map(int,input().split()))
list=[]
for i in range(leng[0]):
    list.append(input())
for i in list:
    print(i[::-1])