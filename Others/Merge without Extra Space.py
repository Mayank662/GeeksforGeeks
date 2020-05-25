t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for j in b:
        a.append(j)
    a.sort()
    print(*a)
