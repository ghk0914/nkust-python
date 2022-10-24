b=input()
for j in range(int(b)):
    a,katachi1,katachi2=map(str,input().split())
    a=int(a)
    for i in range(1,a+1):
        print(i*katachi1,end="")
        print((a-i)*katachi2)