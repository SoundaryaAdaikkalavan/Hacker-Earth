def findSeat(f):
    seats=[]
    labels=['WS','MS','AS','AS','MS','WS','WS','MS','AS','AS','MS','WS']
    for i in range(1,109,12):
        x = list(range(i,i+12))
        seats.append(x)
    for i in range(len(seats)):
        if f in seats[i]:
            ind = seats[i].index(f)
            seat = seats[i][12-ind-1]
            label = labels[ind]
            break
    return str(seat)+" "+str(label)
 
t=int(input())
for i in range(t):
    f = int(input())
    print(findSeat(f))
