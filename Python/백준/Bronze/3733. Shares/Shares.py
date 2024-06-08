while True:
    try:  
        a = list(map(int,input().split()))
        print(a[1]//(a[0]+1))
    except:
        break