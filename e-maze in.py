n=input()
x,y=0,0
for i in n:
    if(i=="L"):
        x,y=x-1,y
    elif(i=="R"):
        x,y=x+1,y
    elif(i=="U"):
        x,y=x,y+1
    else:
        x,y=x,y-1
print(x,y)
