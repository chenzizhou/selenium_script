#coding: utf8
# 作者：NATURE
# 开发时间：2022/10/11 22:30
# 功能：
import sys
import unittest
from ddt import ddt, data, unpack
import sys
sys.path.append('E:\\python')
from web_automation.waiqin.pageobject.login_page import LoginPage



@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        print('准备')

    @data(('admin', '123456'), ('nature', '123456'))
    @unpack
    def test_01_login(self, username, password):
        '''测试登录'''
        l = LoginPage()
        l.login(username,password)
        self.assertTrue(l.get_expect_element())
        l.close()

    # @unittest.skip #添加改装饰后，测试机也加不进去
    def test_02_login(self):
        print(111222)

    def tearDown(self):
        print('结束')


if __name__ == '__main__':  # 并没有执行
    print(sys.path)
    # suite = unittest.TestSuite()
    # suite=unittest.defaultTestLoader.discover('../testcase','test_login.py')
    # discover.addTest(TestLogin('test_02_login'))
    # # suite.addTest(TestLogin("test_01_login_1"))
    # # runner = unittest.TextTestRunner()
    # file_url='../report/'+time.strftime("%Y-%m-%d %H_%M_%S")+' result.html'
    # print(file_url)
    # f=open(file_url,'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='外勤登录',description='用例执行情况：')
    # runner.run(discover)
    # f.close()
    # send_mail(get_new_file())
    # unittest.main(defaultTest=['TestLogin.test_02_login'],verbosity=2)
    # unittest.main(defaultTest=['TestLogin'],verbosity=2)
