from zuoye1029.BASEPAGE.BasePage import *
from selenium.webdriver.common.by import By
from time import sleep
class page(basepage):
    aa = ''
    get_X =By.XPATH
    get_I =By.ID
    get_N =By.NAME
    get_T =By.PARTIAL_LINK_TEXT
    get_P =By.LINK_TEXT
    get_C =By.CSS_SELECTOR
    get_S =By.CLASS_NAME
    get_ss = 'key'
    get_an = '//*[@id="search"]/div/div[2]/button'
    get_sp ='#J_goodsList > ul > li:nth-child(1) > div > div.p-img > a > img'
    get_dl ='//*[@id="ttbar-login"]/a[1]'
    get_zd ='#content > div.login-wrap > div.w > div > div.login-tab.login-tab-r > a'
    get_zh ='loginname'
    get_mm ='nloginpwd'
    get_da ='loginsubmit'
    get_dy ='//*[@id="281047881"]/div/div[1]/div/div/div/img'
    def ele1(self):
        self.click_(self.get_X, page.get_dl)
        sleep(1)
        self.win_to()
        sleep(1)
        self.click_(self.get_C, page.get_zd)
        sleep(1)
        self.send_keys_(self.get_I, page.get_zh, '17545501710')
        sleep(1)
        self.send_keys_(self.get_I, page.get_mm, '123456789..')
        sleep(1)
        self.click_(self.get_I, page.get_da)
        sleep(3)

    def ele2(self,t):
        self.win_to()
        sleep(1)
        self.send_keys_(self.get_I, page.get_ss, t)
        sleep(1)
        self.click_(self.get_X, page.get_an)
        sleep(1)
        self.win_to()
        sleep(1)
        self.scrollTo500()
        sleep(1)
        self.click_(self.get_C, page.get_sp)
        sleep(3)
        self.aa = self.find_ele(self.get_X,page.get_dy).is_displayed()
        sleep(1)


