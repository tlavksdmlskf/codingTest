while True:
    a = int(input())
    if (a == 0):
        break
    else:
        for i in range(1, a + 1):
            print("*" * i)