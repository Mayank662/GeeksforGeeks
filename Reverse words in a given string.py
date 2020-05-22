t=int(input())
for i in range(t):
    s=input()
    a=s.split(".")
    a.reverse()
    s=""
    a=s.join(a)
    a=a.replace(" ",".")
    print(*a)
