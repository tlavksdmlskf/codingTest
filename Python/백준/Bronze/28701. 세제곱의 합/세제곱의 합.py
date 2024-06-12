num = int(input())+1
print(sum(i for i in range(1,num)))
print(pow(sum(i for i in range(1, num)),2))
print(sum(pow(i,3) for i in range(1,num)))