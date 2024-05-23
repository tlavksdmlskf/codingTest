a = input()
istrue = 0
for i in range(len(a)):
    if a[i] == a[len(a) - i - 1]:
        isTrue = 1
    else:
        isTrue = 0
        break
print(isTrue)
