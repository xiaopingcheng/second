from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import  sleep
from selenium.webdriver.support.ui import WebDriverWait

class login(Page):
    '''
    用户登录页面
    '''
    url= '/'
    #driver = webdriver.Chrome()
    # Action
    #bbs_login_user_loc = (By.XPATH, '//*[@id="mzCust"]/div/div[1]/img')
    #bbs_login_button_loc = (By.ID, 'mzLogin')

    # 邮箱账号登录
    def selectLoginMethod(self):
        ele0 = self.driver.find_element_by_id('lbNormal')
        ActionChains(self.driver).move_to_element(ele0).perform()

    # def bbs_login(self):
    #     ele1 = self.find_element(*self.bbs_login_user_loc)
    #     ActionChains(self.driver).move_to_element(ele1).perform()
    #     self.driver.implicitly_wait(2)
    #     self.find_element(*self.bbs_login_button_loc).click()

    # 切到登录的帧里
    def switchToFrame(self):
        self.driver.switch_to.frame('x-URS-iframe')

    login_username_loc = (By.NAME, 'email')
    login_password_loc = (By.NAME, 'password')
    login_button_loc = (By.ID, 'dologin')

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    # //*[@id="captcha2"]/div/div[2]/div[2]/div/div[2]/span
    # 等待验证码验证完成
    #     self.driver.implicitly_wait(30)
    #     self.driver.find_element_by_xpath('//*[@id="captcha2"]/div/div[2]/div[2]/div/div[2]/span')

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def user_login(self, username = 'username', password = '1111'):
        '''获取的用户名密码登录'''
        self.open()
        sleep(2)
        #self.bbs_login()
        self.switchToFrame()
        self.login_username(username)
        self.login_password(password)
        # #WebDriverWait(self.driver, 10).until(lambda driver:
        #                                      self.driver.find_element_by_class_name
        #                                      ('geetest_success_radar_tip_content'))
        self.login_button()
        sleep(4)
    #用户登录成功后，我的账户提示
    def user_login_success(self):
        ele2 = self.driver.find_element_by_class_name('nui-faceEdit-tips')
        ActionChains(self.driver).move_to_element(ele2).perform()
        sleep(2)
        return (self.driver.find_element_by_class_name('nui-faceEdit-tips').text + '登录成功')