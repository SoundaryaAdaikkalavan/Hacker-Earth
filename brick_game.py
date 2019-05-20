n = int(input())
s =0
count =0 
while s<n:
    count = count+1
    s = s + 3*count 
    
s = s-3*count
if n-s<=count:
    print('Patlu')
else:
    print('Motu')
