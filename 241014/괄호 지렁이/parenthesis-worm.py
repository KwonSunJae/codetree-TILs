import sys

input = sys.stdin.readline

N = int(input())

maps = [[0 for _ in range(N)] for _ in range(N)]
for r in range(N):
    row = input()
    for c in range(N):
        if row[c] == '(':
            maps[r][c] = 0
        elif row[c]== ')':
            maps[r][c] = 1

dr = [1,-1,0,0]
dc = [0,0,1,-1]
chk= [[False for _ in range(N)] for _ in range(N)]


def backtracking(r,c,upper,depth, maxs):
    res = 0
    #print(r,c,upper,depth,maxs)
    if not upper and depth ==0:
        return maxs*2
    
    cond = False
    if upper:

        for i in range(4):
            
            nr, nc = r+dr[i], c+dc[i]
            if nr >= N or nr <0 or nc >=N or nc <0:
                continue
            
            if maps[nr][nc] == 1:
                continue
            if chk[nr][nc]:
                continue
            
            cond = True
            chk[nr][nc] = True
            res = max(res, backtracking(nr,nc, True, depth+1,maxs+1))
            chk[nr][nc] = False
    

    if not upper or not cond:
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr >= N or nr <0 or nc >=N or nc <0:
                continue
            if maps[nr][nc] == 0:
                continue
            if chk[nr][nc]:
                continue
            chk[nr][nc] = True
            res = max(res, backtracking(nr,nc, False, depth-1,maxs))
            chk[nr][nc] = False
    
    return res

chk[0][0] = True
print(backtracking(0,0,True,1,1))