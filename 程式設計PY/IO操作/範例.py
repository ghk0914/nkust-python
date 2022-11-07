data1=[]
data2=[]
d=1
with open("input.txt","w") as fwrite:##打開文件
    for i in range(1,99):
        fwrite.write(str(i))##寫入文件
        fwrite.write("\n")
    fwrite.write("100\n")
    fwrite.write("99")
    
with open("input.txt","r") as fread:
    data=fread.read().splitlines()##讀取並刪除換行
    ##print(data)
for i in range(0,len(data)):
    data1.append(int(data[i]))
data1.sort()


for i in range(0,len(data1)):
    count=0
    for k in range(1,int(data1[i])):
        # print(data[i])
        # print("k is ",k)
        if(data1[i]%k==0):
            count+=1
            # print("count is ",count)
    if(count==1):
        data2.append(data[i])
data2=list(map(int,data2))#將list裡的str轉int
# print("是質數",end="")
# print(data2)
difference=[x for x in data1 if x not in data2]#對比第一張list與第二張list不同的部分
# print("不是質數",end="")
# print(difference)
difference="\n".join(map(str,difference))#將list轉會為有換行的str
data2="\n".join(map(str,data2))
with open("不是質數.txt","w") as fwrite:
    fwrite.write(difference)
with open("是質數.txt","w") as fwrite:
    fwrite.write(data2)