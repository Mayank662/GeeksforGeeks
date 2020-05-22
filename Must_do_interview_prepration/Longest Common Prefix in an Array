t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    if n==1:
        print(s)
    else:
        a=s.split(" ")
        a=sorted(a,key=len)
        j=0
        p=""
        f=1
        q=len(a[0])
        while(f):
            k=1
            while(k<n and j<q):
                if a[0][j]==a[k][j]:
                    k=k+1
                else:
                    f=0
                    break
            if k==n and j<q:
                p=p+a[0][j]
                j=j+1
            else:
                break
        if p=="":
            print(-1)
        else:
            print(p)
            
