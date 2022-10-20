i=0
while i<11:
    a=input()
    a=a.split(" ")
    c=a[0]
    c=int(c)
    b=a[1]
    b=int(b)
    if c==b:
        print("A tie")
        i+=1
    if c-b==1:
        print("The first man wins the game")
        i+=1
    if b-c==1:
        print("The second man wins the game")
        i+=1
    if c-b==2:
        print("The second man wins the game")
        i+=1
    if b-c==2:
        print("The first man wins the game")
        i+=1

