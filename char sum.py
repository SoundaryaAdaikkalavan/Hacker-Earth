n=input()
c=0
d={}
for i in range(96,123):
    d.update({chr(i):c})
    c+=1
s=0
for j in n:
    for x,y in d.items():
        if(j==x):
            s=s+y
print(s)
