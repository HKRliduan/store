import random
bank ={12345678:{
    "username":"张三",
    "password":123456,
    "country":"中国",
    "province":"北京",
    "street":"昌平老牛湾",
    "tablet":"001",
    "money":1000,
    "bank_name":"中国工商银行昌平支行"
    },87654321:{
    "username":"李四",
    "password":123456,
    "country":"中国",
    "province":"北京",
    "street":"昌平老牛湾",
    "tablet":"002",
    "money":0,
    "bank_name":"中国工商银行昌平支行"
    }
    }
bank_name="中国工商银行昌平支行"
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

def bank_useradd(username,password,country,province,street,tablet,account,money,bank_name):
    if len(bank)>100:
        return 3
    if username in bank:
        return 2
    bank[account]={
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "tablet":tablet,
        "account":account,
        "money":money,
        "bank_name":bank_name
    }
    return 1

def useradd():
    username = input("请输入您的用户名：")
    password = input("请输入您的密码:")
    print("下面请输入您的地址")
    country = input("\t\t请输入您的国籍:")
    province = input("\t\t请输入您的省份:")
    street = input("\t\t请输入您的街道:")
    tablet = input("\t\t请输入您的门牌号: ")
    account = random.randint(10000000, 99999999)
    money = 0

    staus = bank_useradd(username, password, country, province, street, tablet, account, money, bank_name)
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
        print(info % (username, password, account, country, province, street, tablet, money, bank_name))
def cunqian():
    account = int(input("请输入您的账号:"))
    if account in bank:
        cun=int(input("请输入要存入的金额："))
        bank[account]["money"]=int(bank[account]["money"])+cun
        print("您的余额为：", bank[account]["money"])
    else:
        print("您输入的账号不存在")
def qu_money():
    account=int(input('请输入您账号：'))
    if account in bank:
        password=int(input('请输入密码：'))
        if password == bank[account]['password']:
            money=int(input('请输入取款金额：'))
            if money <= int(bank[account]['money']):
                bank[account]['money'] =bank[account]['money'] - money
                info = '''
-----------个人信息----------               
用户名：%s
账号：%s
余额：%s
                '''
                print(info%(bank[account]['username'],account,bank[account]['money']))
            else:
                print("余额不足")
        else:
            print("密码输入错误")
    else:
        print("密码输入错误")

def zhuanz():
    zhuanchu=int(input("请输入转出的账号"))
    if zhuanchu in bank:
        zhuanr=int(input("请输入转入的账号"))
        if zhuanr in bank:
            mima=int(input("请输入转出的密码"))
            if mima==bank[zhuanchu]["password"]:
                zcje=int(input("请输入转出的金额"))
                if zcje<=bank[zhuanchu]["money"]:
                    bank[zhuanchu]["money"]=bank[zhuanchu]["money"]-zcje
                    bank[zhuanr]["money"]=bank[zhuanr]["money"]+zcje
                    info = '''
-----------个人信息----------                    
用户名：%s
账号：%s
余额：%s
'''
                    print(info % (bank[zhuanchu]['username'], zhuanchu , bank[zhuanchu]['money']))
                else:
                    print("您的余额不足！")
            else:
                print("您的密码不正确")
        else:
            print("您输入的转入账号不存在")
    else:
        print("您输入的转出账号不存在")
def chaxun():
    account=int(input("请输入您要查询的账号"))
    if account in bank:
        password=int(input("请输入您的密码"))
        if password == bank[account]["password"]:
            print("12121212")
            info = '''
--------------以下是您的个人信息---------------
用户名：%s
账号：%s
密码：%s
余额：%s
地址：
   国家：%s
   省份：%s
   街道：%s
   门牌号：%s
开户行：%s
--------------------------------------------
                       '''
            print(info %(bank[account]["username"],account,password,bank[account]["money"],bank[account]["country"],
                         bank[account]["province"],bank[account]["street"],bank[account]["tablet"],bank_name))
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
        cunqian()
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