import sys


input = sys.stdin.readline
N = int(input())
maps = {(r,c):0 for r in range(1,101) for c in range(1,101)}

checked = {(r,c):False for r in range(1,101) for c in range(1,101)}

for _ in range(N):
    a,b = map(int,input().split())
    maps[(a,b)] = 1

q = []

for outline in range(1,101): 
    q.append((0,outline))
    q.append((101,outline))
    q.append((outline,0 ))
    q.append((outline,101))

dr = [1,-1,0,0]
dc = [0,0,1,-1]

ans = 0

while q:
    r,c = q.pop()

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if (nr,nc) not in maps.keys():
            continue
        
        if checked[(nr,nc)] :
            continue

        if maps[(nr,nc)] == 1:
            ans += 1
            continue
        
        checked[(nr,nc)] = True
        q.append((nr,nc))

print(ans)