import unittest
from BeautifulReport import BeautifulReport
a = unittest.defaultTestLoader.discover(start_dir=r'D:\untitled2\zuoye1029\TESTCASE',pattern='TestC*')
b =BeautifulReport(a)
b.report('测试报告','r.html','.')