import sys
import bisect
N= int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

ans = 0
for y_idx in range(1,N):
    for x_idx in range(0,y_idx):
        y = arr[y_idx]
        x= arr[x_idx]
        

        

        st_idx = bisect.bisect_left(arr,2*y-x)
        end_idx = bisect.bisect_right(arr,3*y-2*x)

        if st_idx<=y_idx:
            st_idx= y_idx+1
        
        if st_idx > end_idx:
            continue

        ans+= end_idx-st_idx

print(ans)