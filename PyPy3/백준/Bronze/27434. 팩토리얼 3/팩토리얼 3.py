num = int(input()) + 1
result = 1
if num == 1:
    print(1)
else:
    for i in range(1, num):
        result *= i
    print(result)