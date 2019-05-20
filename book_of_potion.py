# Write your code here
n=input()
a=0
for i in range(len(n)):
    a+=int(n[i])*(i+1)
if(a%11==0):
    print("Legal ISBN")
else:
    print("Illegal ISBN")
