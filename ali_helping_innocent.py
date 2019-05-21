s=input()
l="AEIOUY"
if (int(s[0])+int(s[1]))%2==0:
    if (int(s[3])+int(s[4]))%2==0:
        if (int(s[4])+int(s[5]))%2==0:
            if (int(s[7])+int(s[8]))%2==0:
                if s[2] not in l:
                    a=1
                else:
                    a=0
            else:
                a=0
        else:
            a=0
    else:
        a=0
else:
    a=0
if a==1:
    print("valid")
else:
    print("invalid")
