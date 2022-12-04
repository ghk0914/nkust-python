while(True):
    quo=[]
    rem=[]
    i=0
    a,d=map(str,input().split())
    d=int(d)
    if(d<2 or d>10 or int(a)<1):
        break
    # if(d==2):
    #     a=int(a)
    #     binary=format(a,"b")
    #     print(binary)
        # continue
    # if(int(a)<d):
    #     print(a)
    # else:
    if(d>=2):
        quo.append(a)
        quo=list(map(int,quo))
        while(True):
            b=quo[i]/d
            b=int(b)
            if(b==0):
                break
            c=quo[i]%d
            rem.append(c)
            quo.append(b)
            # print("quo=",quo)
            # print("rem=",rem)
            if(b<d-1):
                break
            i+=1
        print(quo[len(quo)-1],end="")
        for i in range(len(rem),0,-1):
            print(rem[i-1],end="")
        print()

