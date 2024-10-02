import sys

input= sys.stdin.readline

N = int(input())
coor = {}
for _ in range(N):
    x,y = map(int,input().split())
    coor[(x,y)] = 0

def get_dir(x,y,nx,ny):
    if ny > y :
        return 0
    elif ny < y:
        return 2

    if nx > x:
        return 1
    elif nx < x:
        return 4


def backtracking(x,y,depth,dirs):
    if depth == N and (x==0 or y == 0) and dirs != get_dir(x,y,0,0):
        return 1

    sums = 0
    for k in coor.keys():
        if coor[k] == 1:
            continue
        if not (k[0] == x or k[1] ==y):
            continue
        if dirs == get_dir(x,y,k[0],k[1]):
            continue

        coor[k] = 1
        sums += backtracking(k[0],k[1],depth+1,get_dir(x,y,k[0],k[1]) )
        coor[k] = 0
    
    return sums

print(backtracking(0,0,0,-1))