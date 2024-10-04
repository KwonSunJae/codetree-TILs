import sys

input = sys.stdin.readline
N = 0
S = 2
E = 1
W = 3

query = input()
dp = [(0,0,N)]*4*len(query)

def add_d(x,y,d,dx,dy,dd):
    if (4+d)%4 == N :
        return (x+dx,y+dy,(4+dd)%4)
    elif (4+d)%4 == S:
        return (x-dx,y-dy,(4+S+dd)%4)
    elif (4+d)%4 == E:
        return (x+dy,y-dx ,(4+E+dd)%4)
    else :
        return (x-dy,y+dx,(4+W+dd)%4)

def init_query(node,start,end):
    if start == end:
        if query[start] == 'F':
            dp[node]=(0,1,0)
            
        elif query[start] == 'L':
            dp[node]=(0,0,-1)
            
        elif query[start] == 'R':
            dp[node]=(0,0,1)
        return dp[node]
    elif start> end:
        return (0,0,0)
    mid = (start+end)//2
    left_node = init_query(node*2,start,mid)
    rifht_node = init_query(node*2+1, mid+1,end)

    x,y,d = left_node
    dx,dy,dd = rifht_node
    dp[node]=add_d(x,y,d,dx,dy,dd)
    return dp[node]

def go_query(left,right,start,end,node):
    if left > end or right < start:
        return (0,0,0)
    if left<=start and right >= end:
        return dp[node]
    mid = (start+end)//2
    left_node = go_query(left,right,start,mid,node*2)
    rifht_node = go_query(left,right, mid+1,end,node*2+1)
    x,y,d = left_node
    dx,dy,dd = rifht_node
    return add_d(x,y,d,dx,dy,dd)
L = len(query)
init_query(1,0,L-1)


res=[]

for i in range(L):
    print(ord(query[i]))
    tx,ty,td = go_query(0,i-1,0,L-1,1)
    #print(tx,ty,td)
    dx,dy,dd = go_query(i+1,L-1,0,L-1,1)
    #print(dx,dy,dd)
    temp1,temp2 = (0,0,0),(0,0,0)
    if query[i] == 'F':
        temp1,temp2=(0,0,-1),(0,0,1)          
    elif query[i] == 'L':
        temp1,temp2=(0,1,0),(0,0,1)
    elif query[i] == 'R':
        temp1,temp2=(0,0,-1),(0,1,0)
    else:
        continue
    
    x,y,d = add_d(tx,ty,td,temp1[0],temp1[1],temp1[2])
    
    nx,ny,nd = add_d(x,y,d,dx,dy,dd)
    res.append((nx,ny))
    x,y,d = add_d(tx,ty,td,temp2[0],temp2[1],temp2[2])
    
    nx,ny,nd = add_d(x,y,d,dx,dy,dd)
    res.append((nx,ny))
#print(res)
print(len(set(res)))