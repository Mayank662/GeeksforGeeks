t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if k==1:
        print(min(a[0],b[0]))
    else:
        q=0
        p=0
        x=0
        while (p<n and q<m) and x!=k:
            if a[p]<=b[q]:
                z=a[p]
                p=p+1
                x=x+1
            else:
                z=b[q]
                q=q+1
                x=x+1
        while (p<n) and x!=k:
            z=a[p]
            p=p+1
            x=x+1
        while (q<m) and x!=k:
            z=b[q]
            q=q+1
            x=x+1
            
        print(z)
                
                
