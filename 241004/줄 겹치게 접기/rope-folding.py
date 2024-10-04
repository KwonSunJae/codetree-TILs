import bisect

import sys


input = sys.stdin.readline

 
N,L = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

start,end = 0,L
cnt = 0
arr.sort()

while start != end:
    mid = (start+end)/2
    cnt +=1
    mid_idx = bisect.bisect_left(arr,mid)
    #print(mid_idx,mid)


    flag = True

    if 2*mid_idx > N:
        flag = False

    for i in range(1,mid_idx):
        if not flag:
            break
        if mid-arr[i] != arr[mid_idx+(mid_idx-i)]-mid :
            flag = False
            break

    if not flag:
        end = arr[N-cnt]
    else:
        print((mid_idx+1)*2)
        break