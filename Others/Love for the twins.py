t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    j=0
    s=0
    p=[]
    while(j<n-1):
        if a[j]==a[j+1]:
            s=s+1
            j=j+2
        else:
            p.append(a[j])
            j=j+1
    j=0
    while(j<len(p)-1):
        
            
