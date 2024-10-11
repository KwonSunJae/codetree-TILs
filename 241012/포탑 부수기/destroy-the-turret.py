import collections
import heapq

import sys
import itertools

N,M,K = map(int,input().split())

maps = { (r,c): 0 for r in range(N) for c in range(M)}

time = 0
for r in range(N):
    row = list(map(int,input().split()))
    for c in range(M):
        maps[(r,c)] = (row[c],time)
        if row[c] == 0 :
            del maps[(r,c)]
            #able[(r,c)]  = row[c]
            # heapq.heappush(wq,(row[c],-1* time, -1 * (r+c), -1 * c,(r,c))))
            # heapq.heappush(sq,(-row[c],time, r+c, c,(r,c)))


def get_weak():

    res = [(maps[k][0], maps[k][1]*-1,-1*sum(k),-1*k[1],k) for k in maps.keys()]
    #print(res)
    heapq.heapify(res)
    #print(res)
    return heapq.heappop(res)[-1]

def get_strong():
    res = [(-1* maps[k][0], maps[k][1],sum(k),k[1],k) for k in maps.keys()]
    heapq.heapify(res)
    return heapq.heappop(res)[-1]

def calc_shortest_path(a,b):

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    checked= { (r,c): False for r in range(N) for c in range(M)}
    q= collections.deque()
    q.append((a,[]))
    checked[a] = True

    while q :
        k,path = q.popleft()

        if k == b:
            return path
        for i in range(4):
            nr,nc = (N+k[0]+dr[i])%N, (M+k[1] + dc[i])%M

            if (nr,nc) not in maps:
                continue

            if checked[(nr,nc)]:
                continue
            
            
            checked[(nr,nc)] = True
            q.append(((nr,nc),path+[(nr,nc)]))
    
    return []

def print_maps():
    for r in range(N):
        ans = ""
        for c in range(M):

            if (r,c) not in maps:
                ans +='0 '
            else :
                ans += str(maps[(r,c)][0]) + " "
        
        print(ans)

def calc_8(a,b):

    r,c = b

    dr = [-1,-1,-1,0,0,0,1,1,1]
    dc = [-1,0,1,-1,0,1,-1,0,1]
    res = []
    for i in range(9):
        nr,nc = (N+r+dr[i])%N,(M+c+dc[i])%M

        if (nr,nc) not in maps:
            continue
        if (nr,nc) == a:
            continue
        res.append((nr,nc))
    return res

for k in range(1,K+1):
    # 공격자 선정
    attacker, attacked= get_weak(), get_strong()

    if attacker == attacked:
        break

    power = maps[attacker][0] + N+M
    #print(attacker,attacked,power)
    attack_lis  = calc_shortest_path(attacker,attacked)
    

    if not attack_lis:
        attack_lis = calc_8(attacker,attacked)

    
    #print("attak lis", attack_lis)

    for a in attack_lis:
        if a == attacked or a == attacker:
            continue 

        p,t = maps[a]
        if p <= power//2 :
            del maps[a] 
        else :
            maps[a] = (p-power//2,t)
            
    
    if maps[attacked][0] <= power:
        del maps[attacked]
    else:
        maps[attacked] = (maps[attacked][0]-power,maps[attacked][1])
        
    maps[attacker] = (power,k)


    for a in maps.keys():
        if a in attack_lis:
            continue
        if a == attacked or a == attacker:
            continue 
        maps[a] =  (maps[a][0]+1 ,maps[a][1])
    
    
    #print_maps()
        

print(max([maps[k][0] for k in maps.keys()]))