a=input()
s=''
for i in a:
    if i.isupper():
        d=i.lower()
        s=s+d 
    else:
        d=i.upper()
        s=s+d
print(s)
