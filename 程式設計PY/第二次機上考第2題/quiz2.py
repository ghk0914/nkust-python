import random
base=[]
# with open("input.txt","w") as f:
#     for i in range(5):
#         x=random.randrange(1,101)
#         f.write(str(x))
#         f.write("\n")

with open("input.txt","r") as f:
    base=f.read().splitlines()
base=list(map(int,base))
print(base)

for i in range(0,len(base)):
    data=[]
    data2=[]
    if(base[i]<1):
        continue
    for j in range(1,base[i]+1):
        if(base[i]%j==0):
            if(j%2!=0):
                data.append(j)
    data2=" ".join(map(str,data))
    with open("output.txt","a") as f:
        f.write(data2)
        f.write("\n")
    for i in range(0,len(data)):
        print(data[i],end=" ")
    print()
