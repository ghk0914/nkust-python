for i in range(10):
    testdata=[]
    a,b,c=map(int,input().split())
    testdata.append(a)
    testdata.append(b)
    testdata.append(c)
    list1=[]
    list2=[]
    list3=[]
    if testdata[0]==1:
        for i in range(1,101):
            if testdata[1]%i==0:
                list1.append(i)
        for i in range(1,101):
            if testdata[2]%i==0:
                list2.append(i)
    else:
        for i in range(1,101):
            if i%testdata[1]==0 and i%testdata[2]==0:
                list3.append(i)
        if len(list3)==0:
            print("None")    
    common_multiple=' '.join(map(str,list3))
    same=[x for x in list1 if x in list2]
    same1=same
    same=' '.join(map(str,same1))
    print(same)
    print(common_multiple)
        


