# Write your code here
n=int(input())
for i in range(0,n):
    sh,sm,eh,em=map(int,input().split())
    a=sh*60
    s=a+sm
    b=eh*60
    e=b+em
    hour=e-s
    hour1=hour//60
    mint=hour%60
    print(hour1,mint)
