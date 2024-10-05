import bisect

import sys


input = sys.stdin.readline

 
N,L = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

start,end = 0,L
cnt = 1
arr.sort()

ans = 0
while start != end:
    if cnt >= N :
        break
    mid = (start+end)/2
    mid_idx = bisect.bisect_right(arr,mid)

    flag = True

    if 2*mid_idx > N:
        
        flag = False

    for i in range(1,mid_idx):
        if not flag:
            break
        #print(mid-arr[i],arr[mid_idx+(mid_idx-i-1)]-mid)
        if mid-arr[i] != arr[mid_idx+(mid_idx-i-1)]-mid :
            flag = False
            break
    
    if not flag:
        end = arr[N-cnt]
    else:
        ans +=mid_idx
    cnt +=1
        
print(ans)