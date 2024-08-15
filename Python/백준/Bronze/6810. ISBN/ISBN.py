a = []

for _ in range(3):
    a.append(int(input()))

print("The 1-3-sum is", (9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3 + a[0] * 1 + a[1] * 3 + a[2] * 1))