
data=[[0]*4 for i in range(100)]
while(True):
    cous=list(map(str,input().split()))
    mode=cous[0]
    if(mode=="*"):
        break
    else:
        id=int(cous[1])
        if(mode=="@"):
            if((data[id][0])!=0):
                print("Exist")
            else:
                for i in range(0,4):
                    data[id][i]=cous[i+1]

        if(mode=="#"):
            if(data[id][0]==0):
                print("None")
            else:
                for i in range(0,4):
                    data[id][i]=0

        if(mode=="!"):
            chang=int(cous[2])
            if(data[id][0]==0):
                print("None")
            else:
                data[id][chang+1]=cous[3]

        if(mode=="$"):
            chang=int(cous[2])
            if(data[id][0]==0):
                print("None")
            else:
                print(data[id][chang+1])
