print("==============猜字游戏=============")
print("猜对加150元，猜错减100元，数字在0-50之间哦！")
print("首充100元，送初始金额:500元")
import random
ran=random.randint(0,50)
A=500
i=1
print(ran)
while i<=3 or A<100:
    num=int(input("请输入一个数字:"))
    if num==ran:
        print("ok")
        A=A+150
        i=i+1
        print("初始金额:",A)
    elif num>ran:
        print("猜大了")
        A=A-100
        i=i+1
        print("初始金额:",A)
    elif num<ran :
        print("猜小了")
        A = A - 100
        i = i + 1
        print("初始金额:", A)
    if A<100:
        print("游戏结束")
        break


