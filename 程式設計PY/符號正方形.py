def nmsl(a,b,x,y,z,count):
    data=[]
    for i in range(50):
        data.append(x)
        data.append(y)
        data.append(z)
    for i in range(count,b):
        for k in range(count,b):
            s[i][k]=data[b%a]
    return s

while(True):
    a=input()
    a=int(a)
    if(a<1):
        break
    else:
        data=[]
        b=a*2-1
        count=0
        x,y,z=map(str,input().split())
        for i in range(50):
            data.append(x)
            data.append(y)
            data.append(z)

        s=[[0]*b for l in range(b)]

        for i in range(0,a-2):
            s=nmsl(a,b,x,y,z,count)
            count+=1
            b-=1
        for i in range(count,b):
            for k in range(count,b):
                s[i][k]=data[b%a]

        s[a-1][a-1]=x
        for i in range(a*2-1):
            for k in range(a*2-1):
                print(s[i][k],end=" ")
            print()
