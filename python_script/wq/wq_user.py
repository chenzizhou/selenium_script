# Generated by Selenium IDE
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC


class User:
    def __init__(self,url):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.get(url)
        # 刷新当前界面，清除历史数据
        driver.refresh()
        sleep(2)
        # 设置窗口大小
        # driver.set_window_size(1550, 848)
        # sleep(1)
        driver.maximize_window()
        driver.implicitly_wait(20)

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def login(self, username, password):
        sleep(2)
        driver.find_element_by_name("username").send_keys(username)
        sleep(2)
        driver.find_element_by_name('password').send_keys(password)
        sleep(2)
        print('查看密码')
        driver.find_element(By.XPATH,'//div[@class="ey-x-input-suffix"]').click()
        sleep(2)
        print('点击登录')
        driver.find_element(By.XPATH,"//button[text()='登录']").click()
        sleep(2)

    ##  制定方案
    def make_scheme(self, fa_name, fw_name):
        xjgl = driver.find_element_by_xpath('//div/span[@title="巡检管理"]')
        ##鼠标事件 虚浮在元素上方
        ActionChains(driver).move_to_element(xjgl).perform()
        xjfazd = driver.find_element(By.XPATH,
                                     '//span[text()="巡检方案制定"]')
        ActionChains(driver).click(xjfazd).perform()
        sleep(2)
        driver.implicitly_wait(20)
        ##创建方案
        jh_name = fa_name
        print('请输入方案名称')
        driver.find_element_by_xpath('//input[@placeholder="请输入方案名称"]').send_keys(fa_name)
        sleep(2)
        print('点击筛选')
        sx = driver.find_element_by_xpath('//div/a/img[@src="/images/filter.svg"]')
        ActionChains(driver).click(sx).perform()
        sleep(2)
        print('查询范围输入')
        driver.find_element(By.XPATH,"//*[@id='baseInfo']/div[3]/div[1]/span[2]/span/ul").send_keys('04-开关阀组')
        sleep(2)
        print('点击搜索')
        fw = driver.find_element_by_xpath('//*[@id="baseInfo"]/div[4]/div[1]/div[1]/div[2]/i[1]/svg/path')
        ActionChains(driver).click(fw).perform()
        sleep(2)
        ##  随机点击页面 body > div.container-fluid > div.row
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/input').click()
        sleep(2)
        ##搜索
        driver.find_element_by_css_selector('#buttonPanel > input.button.base-button-query-style').click()
        sleep(2)
        ##选择设备
        driver.find_element_by_css_selector(
            '#datagrid-row-r2-2-1 > td:nth-child(1) > div > input[type=checkbox]').click()
        ##点击确定，回到制定界面
        driver.find_element_by_css_selector('#return-bt > input.button.retrieval-button.base-button-save-style').click()
        ##有效范围#workscope2 > xm-select > div.xm-label.single-row
        driver.find_element_by_css_selector('#workscope2 > xm-select > div.xm-label.single-row').click()
        ##备注
        sleep(2)
        driver.find_element_by_css_selector('#form-schemeRemark').send_keys('chenziran')
        ##上报#attachmentfile > div > div:nth-child(1) > div > a > img
        ##保存#saveBut
        driver.find_element_by_css_selector('#saveBut').click()
        ##跳到最外层的页面
        driver.switch_to.default_content()
        driver.find_element_by_css_selector(
            'body > div.v-dialog.v-s-normal.v-t-confirm > div.v-dialog-footer.v-s-center > div.v-dialog-footer-btn.v-dialog-footer-btn-cancel').click()

    def make_plan(self, fa_name, ry_name):
        jh_name = fa_name
        xjgl = driver.find_element_by_xpath('//*[@id="main"]/div[5]/div[2]/div[1]/div/div/div/div[3]/div/span[2]')
        ##鼠标事件 虚浮在元素上方
        ActionChains(driver).move_to_element(xjgl).perform()
        fagl = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/span[2]')
        ActionChains(driver).click(fagl).perform()
        sleep(2)
        driver.find_element_by_css_selector('#horizontal_SearchBar_field-schemeName').send_keys(fa_name)
        sleep(2)
        ##点击查询 #query
        driver.find_element(By.XPATH,"//span[contains(@style,'search')]").click()
        ##点击分派
        sleep(2)
        driver.find_element(By.XPATH,"//td[text()='"+fa_name+"测试12']/../td/*/a[text()='分派']").click()
        sleep(2)
        ##切换到制定计划iframe
        jhfp = driver.find_element_by_css_selector(By.XPATH,"//iframe[contains(@src,'assignmentTask')]")
        driver.switch_to.frame(jhfp)
        sleep(2)
        driver.find_element_by_css_selector('#taskName').send_keys(jh_name)
        sleep(2)
        ##人员选择 exeUserPerson
        driver.find_element_by_id('exeUserPerson').click()
        ##跳到最外层的页面
        driver.switch_to.default_content()
        sleep(2)
        ryxz = driver.find_element_by_css_selector('#layui-laydialog-iframe1')
        driver.switch_to.frame(ryxz)
        driver.find_element_by_css_selector('#fullname').send_keys(ry_name)
        print('点击搜索')
        driver.find_element(By.XPATH,"//span[text()='搜索']").click()
        print('选择人')
        driver.find_element_by_xpath("//td[@title='"+ry_name+"' and contains(@aria-describedby,'name')]").click()
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_link_text('选择').click()
        sleep(2)
        driver.switch_to.frame(jhfp)
        driver.find_element_by_xpath("//input[@value='任务下发']").click()

    def make_ywpz(self,ywlxs,gws,gs=''):
        xtpz = driver.find_elements_by_xpath('//span[@title="系统设置"]')[0]
        # 将业务配置元素滑动到可见位置
        driver.execute_script('arguments[0].scrollIntoView()', xtpz)
        sleep(3)
        ActionChains(driver).move_to_element(xtpz).perform()
        sleep(5)
        elements = driver.find_elements_by_tag_name('span')
        sleep(1)
        for element in elements:
            if element.text == '业务配置':
                print("点击业务配置")
                ActionChains(driver).click(element).perform()
                break
        sleep(2)
        print('进入业务配置')
        # ywlxs=['巡检','养护','检漏','排污稽查']
        for ywlx in ywlxs:
            # 业务配置-查看
            driver.find_element(By.XPATH,r"//td[text()='"+ywlx+"']/../td[3]/div/button[1]").click()
            print("进入业务配置列表")
            driver.find_element_by_xpath('//div[text()="+ 添加类型"]').click()
            sleep(2)
            if gs:
                driver.find_element_by_id('name').send_keys(gs+'-'+ywlx)
                sleep(1)
                driver.find_element_by_id('code').send_keys(gs+'-'+ywlx)
            else:
                driver.find_element_by_id('name').send_keys('测试-'+ ywlx)
                sleep(1)
                driver.find_element_by_id('code').send_keys('测试-'+ ywlx)
            # gws = {'北海供水': ['管段', '阀门', '控制阀门', '消防栓', '水表'],'北海原水': ['管段', '渠道', '阀门', '控制阀门', '消防栓'],}
            for gw in gws.keys():
                for sb in gws[gw]:
                    # 添加作业对象
                    driver.find_element_by_xpath("//label[text()='作业对象']/../button[1]").click()
                    sleep(1)
                    # 点击设备类型
                    driver.find_element_by_xpath('//span[@class="ant-select-selection__rendered"]').click()
                    sleep(1)
                    try:
                        # 选择设备
                        driver.find_element(By.CSS_SELECTOR, "span[title='" + gw + "']+ul span[title='" + sb + "']").click()
                    except Exception as e:
                        print('------------------无'+gw+'-'+sb+'-----------------------')
                        sleep(1)
                        driver.find_element(By.XPATH,"//span/div/button[@type='submit']/../button[@type='button']").click()
                        sleep(1)
                        continue
                    sleep(1)
                    # 作业历史选择
                    driver.find_element(By.XPATH,
                                        "//div[@id='historyRecords']/div/div[@class='ant-select-selection__rendered']").click()
                    sleep(1)
                    driver.find_element(By.XPATH, "//ul[ @role='listbox']/li[text()='设备作业历史']").click()
                    sleep(1)
                    # 到位
                    driver.find_element(By.XPATH, "//span[text()='到位']").click()
                    sleep(1)
                    # 到位半径
                    dwbj=driver.find_element(By.XPATH, "//input[@role='spinbutton']")
                    dwbj.send_keys(Keys.CONTROL,'a')
                    sleep(1)
                    dwbj.send_keys(100)
                    sleep(1)
                    # 是否反馈
                    # driver.find_element(By.XPATH, "//span[text()='反馈']").click()
                    # 设备反馈
                    # driver.find_element(By.XPATH,"//div[@id='equipFeedbackBpm']/div/div[@class='ant-select-selection__rendered']").click()
                    # sleep(2)
                    # 设备流程
                    # driver.find_element(By.XPATH, "//ul[@role='listbox']/li[text()='设备反馈']").click()
                    # sleep(1)
                    # 保存
                    driver.find_element(By.XPATH, "//span/div/button[@type='submit']").click()
                    try:
                        n = 1
                        while driver.find_element(By.XPATH,"//span[text()='作业对象重复,请重新输入']"):
                            driver.find_element(By.XPATH,"//*[@id='objectName']").send_keys(n)
                            n+=1
                            driver.find_element(By.XPATH, "//span/div/button[@type='submit']").click()
                    except Exception as e:
                        pass
                    finally:
                        print(f'{gw}-{sb}已添加！')
                        continue
                print(gw+' 所有设备已添加完毕！')
            driver.find_element_by_xpath('//span/button[1]').click()