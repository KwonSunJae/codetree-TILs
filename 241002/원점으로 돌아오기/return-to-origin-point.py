import sys

input= sys.stdin.readline

N = int(input())
coor = {}
for _ in range(N):
    x,y = map(int,input().split())
    coor[(x,y)] = 0

def backtracking(x,y,depth):
    if depth == N and (x==0 or y == 0):
        return 1

    sums = 0
    for k in coor.keys():
        if coor[k] == 1:
            continue
        if not (k[0] == x or k[1] ==y):
            continue

        coor[k] = 1
        sums += backtracking(k[0],k[1],depth+1)
        coor[k] = 0
    
    return sums

print(backtracking(0,0,0))