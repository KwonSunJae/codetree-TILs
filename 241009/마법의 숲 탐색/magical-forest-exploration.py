import sys
import collections
NTH = 0
EST = 1
STH = 2
WST = 3

EMPT = 0
GRLM = 1
FAIR = 2
EXIT = 3

input = sys.stdin.readline

R,C,K = map(int,input().split())
## 골렘은 십자 모양의 구조를 가지고 있으며, 중앙 칸을 포함해 총 5칸을 차지합니다
maps = {(r,c):(EMPT,0) for r in range(-2,R+1) for c in range(1,C+1)}
## i번째로 숲을 탐색하는 골렘은 숲의 가장 북쪽에서 시작해 골렘의 중앙이 ci 열이 되도록 하는 위치에서 내려오기 시작합니다.

dr = [-1,0,1,0]
dc = [0,1,0,-1]


def get_grlm_pos(r,c,d):
    res = []
    for i in range(4):
        res.append((dr[i]+r,dc[i]+c,True if d==i else False))
    return res

def get_turn_wst_grlm_pos(r,c,d):
    
    c = c-1
    res = []
    for i in range(4):
        res.append((dr[i]+r,dc[i]+c,True if (4+d-1)%4==i else False))

    r = r+1
    for i in range(4):
        res.append((dr[i]+r,dc[i]+c,True if (4+d-1)%4==i else False))
    return list(set(res))

def get_turn_est_grlm_pos(r,c,d):
    res = []
    
    c = c+1
    for i in range(4):
        res.append((dr[i]+r,dc[i]+c,True if (d+1)%4==i else False))
    r = r+1
    for i in range(4):
        res.append((dr[i]+r,dc[i]+c,True if (d+1)%4==i else False))

    return list(set(res))

def go_down_until_block(r,c,d):
    
    while True:
        for (nr,nc,_) in get_grlm_pos(r+1,c,d):
            if (nr,nc) not in maps:
                
                return (r,c)

            if maps[(nr,nc)][0] !=0 :
                
                return (r,c)

        r+=1


def determine_pos(r,c,d,idx):
    #print("det Pos",r,c,d,idx)
    for (nr,nc,ext) in get_grlm_pos(r,c,d):
        if ext :
            maps[(nr,nc)] = (EXIT,idx)
        else :
            maps[(nr,nc)] = (GRLM,idx)
    maps[(r,c)] = (FAIR,idx)

def simulate(r,c,d,idx):
    flag = True
    cr,cc,cd = r,c,d
    cnt = 0
    while flag:

        nr,nc = go_down_until_block(cr,cc,cd)
        #print("godown",nr,nc)
        if (nr,nc) == (r,c):
            flag = False
            
        else :
            cr,cc = nr,nc
            cnt +=1
        
        
        flag = True

        for (nr,nc,exit) in get_turn_wst_grlm_pos(cr,cc,cd) :
            if (nr,nc) not in maps:
                flag = False
                break

            if maps[(nr,nc)][0] != 0:
                flag = False
                break
        
        if not flag :
            #print(get_turn_est_grlm_pos(cr,cc,cd))
            flag = True
            for (nr,nc, exit) in get_turn_est_grlm_pos(cr,cc,cd):
                #print("pass")
                if (nr,nc) not in maps:
                    flag = False
                    break

                if maps[(nr,nc)][0] != 0:
                    flag = False
                    break
            if flag :
                #print("turn right")
                cr,cc,cd = cr+1,cc+1,(cd+1)%4
                cnt+=1
            else:
                if cnt == 0 :
                    return (-1,-1,-1)
            
            
        else :
            #print("turn left")
            cr,cc,cd = cr+1,cc-1,(4+cd-1)%4
            cnt +=1


    determine_pos(cr,cc,cd,idx)
    return (cr,cc,cd)



def print_map():
    for r in range(1,R+1):
        ans = ''
        for c in range(1,C+1):
            ans += str(maps[r,c]) 
        print(ans)

def where_exit(r,c,d):
    if d == NTH:
        return (r-1,c)
    elif d == STH :
        return (r+1,c)
    elif d== EST:
        return (r,c+1)
    elif d == WST:
        return (r,c-1)
    else:
        return (-1,-1)

arr = []


def bfs(idx):
    tr,tc,td = arr[idx]
    #print(arr)
    maxs = tr + 1
    q = collections.deque()
    q.append( where_exit(tr,tc,td))
    checked=[False for _ in range(idx+1)]
    checked[idx] = True
    while q:
        r,c = q.popleft()
        #print("check",r,c)
        #print(checked)
        if maxs == R:
            return R
        for i in range(4):
            nr ,nc = r + dr[i], c + dc[i]
            if not (nr,nc) in maps:
                #print("not key")
                continue
            types,nidx =  maps[(nr,nc)]
            #print(nr,nc,nidx,types)
            if types > EMPT and not checked[nidx]:
                
                checked[nidx] = True
                nr,nc,nd = arr[nidx]
                maxs = max(maxs,nr+1)
                q.append(where_exit(nr,nc,nd))
            
    return maxs



ans = 0
for i in range(K):
    c,d = map(int,input().split())
    arr.append(simulate(-1,c,d,i))
    if arr[-1][0] <= 1:
        maps = {(r,c):(EMPT,0) for r in range(-2,R+1) for c in range(1,C+1)}
        continue
    
    ans += bfs(i)

    #print_map()
    #print(ans)

print(ans)