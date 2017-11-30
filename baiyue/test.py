import os

from time import sleep
from appium import webdriver

apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径
# print(apk_path)

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '4.4.2'  # 设备系统版本
desired_caps['deviceName'] = '127.0.0.1:66021'  # 设备名称

# 测试apk包的路径
desired_caps['app'] = apk_path + '\\baiyue.apk'
# desired_caps['app'] = "E:\\baiyue.apk"

# 是否需要每次都安装apk
desired_caps['noReset'] = False

# 应用程序的包名 aapt dump badging xx.apk
desired_caps['appPackage'] = 'com.baidu.yuedu'
desired_caps['appActivity'] = 'com.baidu.yuedu.splash.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app

driver.wait_activity(".base.ui.MainActivity",30)

# 判断dialog是否弹出
dialog = driver.find_element_by_id("com.baidu.yuedu:id/btn_cancel")
if dialog:
    dialog.click()

# confirm = driver.find_element_by_id("com.baidu.yuedu:id/positive")
# if confirm:
#     confirm.click()

# 进入我的
driver.find_element_by_id("com.baidu.yuedu:id/useraccount_title").click()

# 立即登录
driver.find_element_by_id("com.baidu.yuedu:id/yt_account_login").click()

# 检索百度账号登录
et = driver.find_elements_by_class_name("android.widget.EditText")
et[0].clear()
et[0].send_keys("szz1298@126.com")
et[1].clear()
et[1].send_keys("szzhe5067")
driver.find_element_by_class_name("android.widget.Button").click()


try:
    assert "szz1298" in driver.page_source
except AssertionError as err:
    print ('Exception: ', err)
else:
    print ("no errors")

sleep(5)

driver.quit()
