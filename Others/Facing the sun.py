t=int(input())
for i in range(t):
    n=int(input())
    h=list(map(int,input().split()))
    k=0
    m=h[0]
    for j in range(1,n):
        if(h[j]>m):
            k=k+1
            m=h[j]
    k=k+1
    print(k)
