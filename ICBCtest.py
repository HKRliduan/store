from HTMLTestRunner import HTMLTestRunner
import unittest
import os # 系统
from threading import Thread

class icbc(Thread):
    pettern=""
    description=""
    file=""
    def run(self) -> None:
        # 加载所有用例
        tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern=self.pettern)

        # 执行器
        runner = HTMLTestRunner.HTMLTestRunner(
            title="工商银行测试报告",
            description=self.description,
            verbosity=1,
            stream=open(file=self.file, mode="w+", encoding="utf-8")
        )
        runner.run(tests)
att1=icbc()
att1.pettern="testaddUser.py"
att1.description="中国工商银行开户测试报告"
att1.file="中国工商银行开户测试报告.html"
att2=icbc()
att2.pettern="testsaveMoney.py"
att2.description="中国工商银行存钱测试报告"
att2.file="中国工商银行存钱测试报告.html"
att3=icbc()
att3.pettern="testtakeMoney.py"
att3.description="中国工商银行取钱测试报告"
att3.file="中国工商银行取钱测试报告.html"
att4=icbc()
att4.pettern="testtransformMoney.py"
att4.description="中国工商银行转账测试报告"
att4.file="中国工商银行转账测试报告.html"
att1.start()
att2.start()
att3.start()
att4.start()
















