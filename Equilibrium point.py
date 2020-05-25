t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for j in range(n):
        s=s+a[j]
    l=0
    f=1
    j=0
    while(j<n and f):
        s=s-a[j]
        if s==l:
            print(j+1)
            f=0
        else:
            l=l+a[j]
        j=j+1
    if f==1:
        print(-1)
