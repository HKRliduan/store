from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_saveMoney
from unittest import TestCase



da=[
    [123456789, 5000, True],
    [123456780, 5000, False],
    [123456789,-1000,False],
    [123456789,1000,True]
]
@ddt
class TestBank(TestCase):
    @data(*da)
    @unpack
    def testsave(self,a,b,c):
        result = bank_saveMoney(a,b)
        self.assertEqual(c,result)