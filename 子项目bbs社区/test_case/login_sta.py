import time
import unittest, random, sys

sys.path.append(r'E:\PycharmProjects\自动化项目实战')
#sys.path.append('./page_obj')
from 自动化项目实战.子项目bbs社区.test_case.page_obj.loginPage import login
from 自动化项目实战.子项目bbs社区.test_case.models import myunit, function


class loginTest(myunit.MyTest):
    '''
    163邮箱自动登录测试
    '''
    def user_login_verify(self, username='', password=''):
        login(self.driver).user_login(username, password)

    def test_login(self):
        self.user_login_verify(username= '13487877976', password='5201xyz123')
        time.sleep(1)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), '点击编辑头像登录成功')
        function.inser_img(self.driver, (time.strftime('%Y-%m-%d-%H-%M-%S') + '_test.png'))

if __name__ == '__main__':
    unittest.main()
