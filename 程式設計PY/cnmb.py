while (True):
    t1 = []
    t2 = []
    O,d1,d2 = map(int,input().split())
    if O==1:
        for a1 in range(1,101):
            if d1%a1==0 and d2%a1==0:
                t1.append(a1)
                t1 = " ".join(map(str,t1))
        print(t1)
    if O==2:
        for a1 in range(1,101):
                if a1%d1==0 and a1%d2==0:
                    t2.append(a1)
        if len(t2)==0:
            print("None")
    t2 = " ".join(map(str,t2))
    print(t2)