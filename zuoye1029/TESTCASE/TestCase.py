from selenium import webdriver
from zuoye1029.PAGE.Page import *
import unittest
import logging
from zuoye1029.common.rizhi.rizhi import *
l = Log('rizhi.log')
l.log()
from zuoye1029.common.xlrdrend import *
x = Read(r'C:\Users\DELL\Desktop\run.xls')
a = x.read()
from ddt import data,ddt
@ddt
class myself(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(r'D:\untitled2\jiaoben\chromedriver.exe')
        cls.driver.get('https://www.jd.com/')
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def test01(self):
        page(self.driver).ele1()
        self.driver.implicitly_wait(5)
        aa = self.driver.current_url
        self.assertNotIn('...',aa)
    @data(*a)
    def test02(self,y):
        page(self.driver).ele2(y)
        logging.info('日志')
        bb = self.driver.title
        self.assertIsNot('sbhgfj',bb)
        self.assertNotEqual('ashf',self.aa)
if __name__ == '__main__':
    # r = unittest.TestSuite()
    # r.addTest(myself.test02)
    # s = unittest.TextTestRunner()
    # s.run(r)
    unittest.main()