# Write your code here
n=int(input())
for i in range(0,n):
    s1,s2=map(str,input().split())
    c=0
    for i in s1:
        if(s2.count(i)==s1.count(i)):
            c+=1
        else:
            break
    if(c==len(s1)):
        print("YES")
    else:
        print("NO")
