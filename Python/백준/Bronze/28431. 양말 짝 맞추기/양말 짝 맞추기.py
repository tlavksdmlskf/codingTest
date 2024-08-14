a = []
for _ in range(5):
    a.append(int(input()))

for i in a:
    if a.count(i) % 2 != 0:
        print(i)
        break

