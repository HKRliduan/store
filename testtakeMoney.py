from ddt import ddt
from ddt import data
from ddt import unpack
from unittest import TestCase
from Bank import bank_takeMoney

da=[
    [123456780,123456,1000,1],
    [123456789,654321,1000,2],
    [123456789,123456,-1,3],
    [123456789,123456,0,0],
    [123456789,123456,1,0],
    [123456789,123456,4999,0],
    [123456788,654321,5001,3],
    [123456788,654321,5000,0],
    ]
@ddt
class TestBank(TestCase):
    @data(*da)
    @unpack
    def testsave(self,a,b,c,d):
        result = bank_takeMoney(a,b,c)
        self.assertEqual(d,result)











