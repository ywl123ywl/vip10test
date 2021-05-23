import unittest
from ddt import ddt,data,unpack


testdata = [[1,2],[3,3]]
testdict = [{'value1':1,'value2':1},{'value1':3,'value2':4}]

@ddt
class MyTest(unittest.TestCase):

    @data((1,1))
    @unpack
    def test_b1(self,value1,value2):
        print('----',value1,value2)
        self.assertEqual(value1,value2)

    @data([1,2],[3,4])
    @unpack
    def test_b2(self, value1, value2):
        print('$$$$', value1, value2)
        self.assertEqual(value1, value2)

    @data(*testdata)
    @unpack
    def test_b3(self, value1, value2):
        print('@@@', value1, value2)
        self.assertEqual(value1, value2)


if __name__ == '__main__':
    unittest.main()