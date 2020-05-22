t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    j=0
    s=0
    m=0
    while(j<n-1):
        if (a[j]+1)==a[j+1]:
            s=s+1
        elif a[j]==a[j+1]:
            s=s
        else:
            if s>m:
                m=s
            s=0
        j=j+1
    if s>m:
        m=s
    print(m+1)
        
