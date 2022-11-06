
def hcf_maker(a,b):
    if(a%1==0 and b%1==0 and a!=0 and b!=0):
        data=[]
        data.append(a)
        data.append(b)
        data.sort()
        for i in range(1,int(data[0]+1)):
            if data[0]%i==0 and data[1]%i==0:
                hcf=i
        hcf=hcf
        return hcf
def lcm_maker(a,b,hcf):
    lcm=a*b/hcf
    return lcm
a=1
b=1
c=1
gain=1
while(gain%1==0 and a%1==0 and b%1==0 and c%1==0 and gain!=0 and a!=0 and b!=0 and c!=0):
    gain,a,b,c=map(float,input().split())
    hcf1=hcf_maker(a,b)
    lcm1=lcm_maker(a,b,hcf1)
    hcf2=hcf_maker(lcm1,c)
    ##print(hcf2)
    lcm2=lcm_maker(lcm1,c,hcf2)
    ##print(int(lcm2))
    if(gain%1!=0):
        break
    gain=int(gain)
    for i in range(1,gain+1):
        LCM=lcm2*i
        print(int(LCM),end=" ")
    print()


