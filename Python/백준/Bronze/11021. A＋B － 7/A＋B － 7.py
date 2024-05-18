import sys
put = sys.stdin.readline().rstrip

length = put()
for i in range(1, int(length) + 1):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print("Case #"+str(i)+":",a+b)

