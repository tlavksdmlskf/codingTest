a = 0
while True:
    try:
        string = input()
        a+=1
    except EOFError:
        break
print(a)