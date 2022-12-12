from math import pow

def rr(d,u,sum1):
    sum1+=pow((d-u),2)
    return sum1

while(True):
    sum2=0
    mylist=list(map(int,input().split()))
    a=mylist[0]
    if(a<=0):
        break
    del mylist[0]
    list_len=len(mylist)
    list_len+=1
    list_len/=2
    list_len=int(list_len)
    mylist.sort()
    mylistlen=len(mylist)
    print(mylist[list_len-1],end=" ")
    sum=0
    for i in range(mylistlen):
        sum+=mylist[i]
    u=sum//(mylistlen)
    for i in range(mylistlen):
        sum2=rr(mylist[i],u,sum2)
    ban_i_su=sum2//(mylistlen)
    ban_i_su=int(ban_i_su)
    print(ban_i_su)