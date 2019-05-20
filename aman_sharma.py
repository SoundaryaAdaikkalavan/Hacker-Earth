n=int(input())
c=0
for i in range(0,n):
    a,b=map(int,input().split())
    a1=2*(22/7)*a
    b1=100*b
    if(a1<=b1):
        c+=1
print(c)
