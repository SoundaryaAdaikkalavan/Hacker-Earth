n=int(input())
m=[6,2,5,5,4,5,6,3,7,6]
for i in range(n):
    a=input()
    c=0
    for j in a:
        c=c+m[int(j)]
    if(c%2==0):
        q=int(c/2)
        print('1'*q)
    else:
        q=int((c-3)/2)
        print('7'+'1'*q)
