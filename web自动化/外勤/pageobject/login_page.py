# coding:utf-8
# 作者：NATURE
# 开发时间：2022/10/11 21:41
# 功能：
from selenium.webdriver.common.by import By

from web自动化.外勤.base.base_page import BasePage


class LoginPage(BasePage):
    # 页面元素
    username_loc = (By.NAME, "username")
    password_loc = (By.NAME, 'password')
    eye_loc = (By.XPATH, '//div[@class="ey-x-input-suffix"]')
    submit_loc = (By.XPATH, "//button[text()='登录']")

    def login(self, username='admin', password='123456'):
        self.send_keys(LoginPage.username_loc, username)
        self.send_keys(LoginPage.password_loc, password)
        self.click(LoginPage.eye_loc)
        self.click(LoginPage.submit_loc)
