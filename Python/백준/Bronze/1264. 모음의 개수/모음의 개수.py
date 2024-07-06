string = input().lower()
while(string!="#"):
    cnt = 0
    for i in string:
        if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
            cnt+=1
    print(cnt)
    string = input().lower()
    