from threading import Thread
import time
basket=0
class chu(Thread):
    nume1=""
    count=0

    def run(self) -> None:
        global basket
        while True:
            if basket <500:
                basket += 1
                self.count += 1
                print(self.nume1,"做了：",self.count,"个")
                if basket==500:
                    time.sleep(3)
                    if basket==500:
                        print(self.nume1, "做了：", self.count, "个")
                        break
class guk(Thread):
    name2=""
    def run(self) -> None:
        global basket
        money=10000
        count1 = 0
        while True:
            if money >0:
                if basket > 0:
                    basket -= 1
                    money -= 5
                    count1 += 1
                    print(self.name2, "抢了", count1, "个，花了", 5 * count1)
                else:
                    time.sleep(3)

            else:
                print(self.name2, "没钱了，一共买了：", count1, "个")
                break

c1=chu()
c1.nume1="大厨"
c2=chu()
c2.nume1="二厨"
c3=chu()
c3.nume1="配菜"
g1=guk()
g1.name2="旺财"
g2=guk()
g2.name2="二哈"
g3=guk()
g3.name2="狗蛋"
g4=guk()
g4.name2="狗剩"
g5=guk()
g5.name2="二狗"
g6=guk()
g6.name2="三驴"
c1.start()
c2.start()
c3.start()
g1.start()
g2.start()
g3.start()
g4.start()
g5.start()
g6.start()
