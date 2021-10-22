from ddt import ddt
from ddt import unpack
from ddt import data
from Bank import bank_addUser
from unittest import TestCase


# username, password, country, province, street, door, money
da=[
    ["二狗子", 123456, "中国", "北京", "沙阳路", "s001", 5000, 1],
    ["二狗子", 123456, "中国", "北京", "沙阳路", "s001", 5000, 2],
    ["二狗子s", 123456, "中国", "北京", "沙阳路", "s001", 5000, 1],
]
@ddt
class TestBank1(TestCase):
    for i in range(96):
        name = "二狗子" + str(i)
        da.append([name,123456,"中国", "北京", "沙阳路", "s001", 5000,1])
    da.append(["二狗子dd",123456,"中国", "北京", "沙阳路", "s001", 5000,3])

    @data(*da)
    @unpack
    def testAddUser(self,a,b,c,d,e,f,g,h):

        s = bank_addUser(a,b,c,d,e,f,g)
        self.assertEqual(h,s)


