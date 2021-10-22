from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_transformMoney
from unittest import TestCase
da=[
    [123456789,123456788,123456,1,0],
    [145454545,123456788,123456,1000,1],
    [123456789,111111111,123456,1000,1],
    [123456789,123456788,654321,5000,2],
    [123456788,123456789,654321,5001,3],
    [123456788,123456789,654321,-1000,3]
]
@ddt
class TestBank(TestCase):
    @data(*da)
    @unpack
    def testsave(self,a,b,c,d,e):
        result = bank_transformMoney(a,b,c,d,)
        self.assertEqual(e,result)


















