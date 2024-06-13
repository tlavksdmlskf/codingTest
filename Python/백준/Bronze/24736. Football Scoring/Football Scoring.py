team1 = list(map(int,input().split()))
team2 = list(map(int,input().split()))

print(sum(((team1[0]*6),(team1[1]*3),(team1[2]*2),(team1[3]*1),(team1[4]*2))), sum(((team2[0]*6),(team2[1]*3),(team2[2]*2),(team2[3]*1),(team2[4]*2))))