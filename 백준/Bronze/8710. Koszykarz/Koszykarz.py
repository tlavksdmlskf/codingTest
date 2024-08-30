import math

a, b, c = map(int, input().split())
cnt = math.ceil((b - a) / c)

print(cnt)