import sys
put = sys.stdin.readline()

length = put.rstrip()
for i in range(int(length)):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)