for frequency in range(3):
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    a=input()
##以下為處理小寫部分
    ##將原始輸入轉ASCII
    for i in range(0,len(a)):
        b.append(ord(a[i]))
    ##計數輸入字元並加入新list
    for j in range (0,len(b)):
        for k in range(97,123):
            c.append(b.count(k))
    ##輸出
    for l in range(0,26):
        if c[l]!=0:
            print(chr(l+97),end=" ")
            for m in range(1,c[l]+1):  
                print("*",end="")
            print(" ",end="")    

##以下為處理大寫部分
    ##將原始輸入轉ASCII
    for I in range(0,len(a)):
        d.append(ord(a[I]))
    ##計數輸入字元並加入list
    for J in range (0,len(d)):
        for K in range(65,91):
            e.append(d.count(K))
    ##輸出
    for L in range(0,26):
        if e[L]!=0:
            print(chr(L+65),end=" ")
            for M in range(1,e[L]+1):
                print("*",end="")
            print(" ",end="")     
    print()