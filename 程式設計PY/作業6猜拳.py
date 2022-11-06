feq=1
while (feq>0):
    feq=input()
    feq=int(feq)
    if (feq%2==0 or feq<1):
        break
    count1=0
    count2=0
    N=(feq+1)/2
    while (count1<N and count2<N):
        one,two=map(str,input().split())
        # print("剪刀Y",ord("Y"))
        # print("石頭M",ord("M"))
        # print("布O",ord("O"))
        one=ord(one)
        two=ord(two)
        if one>two:
            if(one-two==12):
                ##print("2wiin")
                count2+=1
            else:
                ##print("1win")
                count1+=1
        if two>one:
            if(two-one==12):
                ##print("1wiin")
                count1+=1
            else:
                ##print("2win")
                count2+=1
        if(one==two):
            ##print("平手")
            count1+=0
            count2+=0
        ##print("count1=",count1)
        ##print("count2=",count2)  
    if count1>count2:
        print("The first person wins the game")
    else:
        print("The second person wins the game")    
