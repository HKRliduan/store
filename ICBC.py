import random
from DBUtils import update
from DBUtils import select

bank_name = "中国工商银行昌平回龙观支行"

def welcome():
    print("-------------------------------------")
    print("-          中国工商银行昌平支行         -")
    print("-------------------------------------")
    print("-  1 开户                            -")
    print("-  2 存钱                            -")
    print("-  3 取钱                            -")
    print("-  4 转账                            -")
    print("-  5 查询                            -")
    print("-  6 退出                            -")
    print("-------------------------------------")

def getRandom():
    li = "0123456789"
    global string
    string = "6"
    for i in range(18):
        string = string + li[random.randint(0,9)]
    return string

def bank_useradd(username,password,country,province,street,door,money):
    sql1 = "select count(*) from user"
    param1 = []
    data = select(sql1, param1)
    if data[0][0] >= 100:
        return 3
    sql2 = "select * from user where username  = %s"
    param2 = [username]
    data2 = select(sql2, param2)
    if len(data2) != 0:
        return 2
    sql3 = "insert into user  values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
    param3 = [getRandom(), username, password, country, province, street, door, money, bank_name]
    update(sql3, param3)
    return 1

def useradd():
    username = input("请输入您的用户名：")
    password = int(input("请输入您的密码:"))
    print("下面请输入您的地址")
    country = input("\t\t请输入您的国籍:")
    province = input("\t\t请输入您的省份:")
    street = input("\t\t请输入您的街道:")
    door = input("\t\t请输入您的门牌号: ")
    money = 0

    staus = bank_useradd(username, password, country, province, street,door, money)
    if staus == 3:
        print("对不起，用户库已满。")
    if staus == 2:
        print("对不起，该用户已存在，请勿重复开户")
    if staus == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
-----------个人信息----------
用户名：%s
密码：%s
账号：%s
地址信息：
   国家：%s
   省份：%s
   街道：%s
   门牌号：%s
余额：%s
开户行地址：%s
                   '''
        print(info % (username, password, string, country, province, street, door, money, bank_name))
def cun_money():
    account=input("请输入您的账户")
    sql4="select account from user where account =%s"
    param4 = [account]
    data = select(sql4, param4)
    if data[0][0] == account :
        cun = int(input("请输入要存入的金额："))
        sql5="update user set money = money+%s where account =%s "
        param5=[cun,account]
        update(sql5,param5)
        sql6="select money from user where account=%s "
        param6 = [account]
        money=select(sql6, param6)
        money1=money[0][0]
        print("您的余额为：",money1)
    else:
        print("您输入的账号不存在")
def qu_money():
    account = input("请输入您的账户")
    sql4 = "select account,password,username,money from user where account =%s"
    param4 = [account]
    data = select(sql4, param4)
    if data[0][0] == account :
        password=int(input('请输入密码：'))
        if password ==data[0][1] :
            money = int(input('请输入取款金额：'))
            data1=float(data[0][3])
            if money <= data1:
                sql9="update user set money = money-%s where account =%s"
                param9 = [money,account]
                update(sql9, param9)
                sql10 = "select money from user where account =%s"
                param10 = [account]
                data2 = select(sql10, param10)
                info = '''
-----------个人信息----------               
账号：%s
用户名：%s
余额：%s
                '''

                print(info%(account,data[0][2],data2[0][0]))
            else:
                print("余额不足")
        else:
            print("密码输入错误")
    else:
        print("密码输入错误")
def zhuanz():
    account = input("请输入转出的账号")
    sql11 = "select account,password,username,money from user where account =%s"
    param11 = [account]
    data = select(sql11, param11)
    if data[0][0] == account :
        password = int(input('请输入密码：'))
        if password == data[0][1]:
            zhuanr = input("请输入转入的账号")
            sql12 = "select account from user where account =%s"
            param12 = [zhuanr]
            data1 = select(sql12, param12)
            if data1[0][0] == zhuanr :
                zcje=int(input("请输入转出的金额"))
                data2 = float(data[0][3])
                if zcje<=data2:
                    sql13 = "update user set money = money-%s where account =%s"
                    param13 = [zcje, account]
                    update(sql13, param13)
                    sql14 = "update user set money = money+%s where account =%s"
                    param14 = [zcje, zhuanr]
                    update(sql14, param14)
                    sql10 = "select money from user where account =%s"
                    param10 = [account]
                    data3 = select(sql10, param10)
                    info = '''
-----------个人信息----------                    
账号：%s
用户名：%s
余额：%s
'''
                    print(info%(account,data[0][2],data3[0][0]))
                else:
                    print("您的余额不足！")
            else:
                print("您的密码不正确")
        else:
            print("您输入的转入账号不存在")
    else:
        print("您输入的转出账号不存在")
def chaxun():
    account = input("请输入您的账户")
    sql4 = "select * from user where account =%s"
    param4 = [account]
    data = select(sql4, param4)
    if data[0][0] == account:
        password = int(input('请输入密码：'))
        if password == data[0][2]:
            print(data)
        else:
            print("您输入的密码错误")

    else:
        print("您输入的用户不存在")

while True:
    welcome()
    chose = input("请输入您要办理的业务:")
    if chose == "1":
        useradd()
    elif chose == "2":
        cun_money()
    elif chose == "3":
        qu_money()
    elif chose == "4":
        zhuanz()
    elif chose == "5":
        chaxun()
    elif chose == "6":
        print("欢迎下次光临")
        break
    else:
        print("输入错误！请重新输入！")
