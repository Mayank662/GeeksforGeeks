t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=a[n-1]
    p=[a[n-1]]
    if max(a)==m:
        print(m)
    else:
        for j in range(n-2,-1,-1):
            if a[j]>=m:
                m=a[j]
                p.append(m)
        p.reverse()
        print(*p)
            
        
