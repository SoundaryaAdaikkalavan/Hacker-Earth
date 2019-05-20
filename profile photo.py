L=int(input())
N=int(input())
for i in range(0,N):
    w,h=map(int,input().split())
    if(w<L or h<L):
        print("UPLOAD ANOTHER")
    elif(w>=L or h<=L):
        if(w==h):
            print("ACCEPTED")
        else:
            print("CROP IT")
