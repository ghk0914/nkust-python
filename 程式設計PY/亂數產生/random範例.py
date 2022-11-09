import random
x=random.random()#產生0(含)到1之間的浮點數，無法指定範圍
print(x)
x=random.uniform(2.0,8.9)#可指定範圍的產生浮點數亂數 範圍2.0<=x<8.9
print(x)
for i in range(10):
    x=random.randrange(1,26)#可指定範圍 範圍1<=x<26
    print(x)