arr = list(map(int,input().split()))
print("Anything" if arr[1] == arr[2] else "Bus" if arr[1] < arr[2] else "Subway")