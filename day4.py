import random
ran = random.randint(0, 3)
print("==============cs游戏商城=============")
if ran < 1:
    print("恭喜您抽到手榴弹的3折优惠卷")
    Z = 0
else:
    print("恭喜您抽取到火箭筒的9折优惠卷")
    X = 1
shop = [
    ["手榴弹", 500],
    ["手枪", 200],
    ["火箭筒", 1000],
    ["导弹", 50000],
    ["步枪", 500]]
mycat=[]
money = int(input("请输入你的充值金额"))
while True:
    for index, value in enumerate(shop):
        print(index, value)
    A = input("请输入你想要的商品")
    if A.isdigit():
        A = int(A)
        if A > len(shop)-1:
            print("你输入的商品不存在")
            break
        else:
            if money >= shop[A][1] and Z == 0:
                mycat.append(shop[A])
                money = money-(shop[A][1])*0.3
                print("添加成功，已加入购物车")
            elif money >= shop[A][1] and X == 1:
                mycat.append(shop[A])
                money = money-(shop[A][1])*0.9
                print("添加成功，已加入购物车")
            elif money >= shop[A][1]:
                 mycat.append(shop[A])
                 money = money - (shop[A][1])
                 print("添加成功，已加入购物车")
            else:
                print("不好意思，你的钱不够了")
    elif A =="Q" or A =="q":
        print("欢迎下次光临")
        for index,value in enumerate(mycat):
            print(index," ",value)
        print("您的余额剩余：",money,"元")
        break
    else:
        print("输入错误")



