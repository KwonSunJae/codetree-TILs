import bisect

import sys


input = sys.stdin.readline

N,K = map(int,input().split())
arr = []



for _ in range(K):
    a,b = map(int,input().split())

    arr.append((a,b)if a <b else (b,a))
arr.sort(reverse = True)


start, end = i,hate = arr.pop()
ans = 1

while arr:
    i,hate= arr.pop()
    #print(start,end, i, hate)
    if i < end and hate >= end :
        continue
    
    elif i < end and hate < end:
        end = hate
    
    elif i >= end :
        ans +=1
        start = end 
        end = hate
    
if end != N:
    ans +=1
if hate == N:
    ans +=1
print(ans)