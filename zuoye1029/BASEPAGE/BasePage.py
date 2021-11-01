from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class basepage:
    def __init__(self,driver):
        self.driver =driver
    def find_ele(self,b,v):
        self.driver.find_element(b,v)
    def click_(self,b,v):
        self.driver.find_element(b,v).click()
    def send_keys_(self,b,v,t):
        self.driver.find_element(b,v).send_keys(t)
    def win_to(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
    def iframe(self,cc):
        self.driver.switch_to.frame(cc)
    def scrollTo500(self):
        self.driver.execute_script('window.scrollTo(0,500)')
    def scrollTo0(self):
        self.driver.execute_script('window.scrollTo(0,0)')
    def wait_send(self,b,t):
        ele = WebDriverWait(self.driver,10,0.3).until(EC.visibility_of_element_located(*b))
        ele.send_keys(t)
    def con_a(self,b,v):
        #键盘——全选
        self.send_keys_(b,v,(Keys.CONTROL,'a'))
    def clear(self,b,v):
        #键盘——清空
        self.send_keys_(b,v,(Keys.CLEAR))
    def shuangji(self,b,v):
        #鼠标——双击
        a = self.find_ele(b,v)
        ActionChains(self.driver).double_click(a).perform()