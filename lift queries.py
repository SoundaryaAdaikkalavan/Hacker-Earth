n=int(input())
x,y=0,7
for i in range(0,n):
    s=int(input())
    a=abs(y-s)
    b=abs(x-s)
    if(a>=b):
        print("A")
        x=s
    else:
        print("B")
        y=s
