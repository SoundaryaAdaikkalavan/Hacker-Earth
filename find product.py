n=int(input())
a=list(map(int,input().split()))

s=1
for i in a:
  
    
   
    s=(s*i)%(10**9+7)
print(s)
