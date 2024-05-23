a, b = map(int, input()[::-1].split()[::1])

print(a if a >= b else b)