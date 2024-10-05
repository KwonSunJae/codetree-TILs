import sys

input = sys.stdin.readline

N = int(input())

sums= [0 for _ in range(N)]
wildcard = {}
arr = []

for i in range(N):
    a = int(input())
    arr.append(a)
    

def check_list(start):
    target = arr[start]
    wildcard = 0
    lastcard = -1
    lens = 1
    for i in range(start+1,N):
        if i == N-1 and start !=0 and arr[i]==target:
            return (lens+1 ,start)
        if arr[i]!=target :
            if wildcard == 0 or wildcard==arr[i]:
                wildcard = arr[i]
                lastcard = i
            else:
                return (lens,lastcard)

        else :
            lens+=1
    
    return (lens,lastcard)

maxs = 0
i =0
while i < N:
    lens, ended = check_list(i)
    #print(lens, arr[i])
    if ended == -1:
        i +=1
        continue

    maxs = max(lens, maxs)
    i += 1
print(maxs)