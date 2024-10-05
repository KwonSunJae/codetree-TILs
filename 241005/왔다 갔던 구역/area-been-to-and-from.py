import sys
import bisect
import collections


input = sys.stdin.readline

N = int(input())

ll,rr = 0,0
cur = 0


ans = []

def bound(a,b):
    return (a,b) if a < b else (b,a)
for i in range(N):
    
    le, cmd = input().split()
    le = int(le)
    if cmd == "R": 

        if rr < cur+le :
            if cur < rr:

                ans.append(bound(cur,rr)  )
            rr = cur +le
        else:
            ans.append(bound(cur,cur+le))
        
        
        cur = cur + le

        


    elif cmd == "L":
        
        if ll > cur - le :
            if cur > ll:
                ans.append(bound(cur,ll))
            ll = cur - le
        else:
            ans.append(bound(cur-le, cur))

        cur = cur - le
    else :
        continue


def getDist(bounds):
    return bounds[1] - bounds[0]

ans = list(set(ans))
ans.sort()
piv = 0
minl, maxr = ans[piv]
lens = getDist(ans[piv])

#print(ans)
piv+=1
while piv != len(ans):

    ll,rr = ans[piv]
    if ll < maxr and rr <= maxr:
        pass
    elif ll <= maxr and rr > maxr:
        lens += getDist((maxr,rr))
        maxr = rr
    elif ll > maxr  :
        minl,maxr = ans[piv]
        lens += getDist(ans[piv])
    
    piv+=1
    


print(lens)