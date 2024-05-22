alphabet = "abcdefghijklmnopqrstuvwxyz"
arr = [0 for x in range(len(alphabet))]
string = input()

for i in alphabet:
    if i not in string:
        arr[alphabet.index(i)] = -1
    else:
        arr[alphabet.index(i)] = string.index(i)

print(*arr)