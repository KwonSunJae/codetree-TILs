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

lens = 0


def getDist(bounds):
    return bounds[1] - bounds[0]

ans = set(ans)
for s in ans:
    lens += getDist(s)

print(lens)