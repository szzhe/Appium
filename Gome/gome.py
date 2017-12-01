import os
from appium import webdriver
from time import sleep

apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径
# print(apk_path)

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '4.4.2'  # 设备系统版本
desired_caps['deviceName'] = '127.0.0.1:66021'  # 设备名称

# 测试apk包的路径
desired_caps['app'] = apk_path + '\\GomeEShop.apk'
# desired_caps['app'] = "E:\\GomeEShop.apk"

# 是否需要每次都安装apk
desired_caps['noReset'] = True

# 应用程序的包名 aapt dump badging xx.apk
desired_caps['appPackage'] = 'com.gome.eshopnew'
desired_caps['appActivity'] = 'com.gome.ecmall.home.LaunchActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app

driver.wait_activity("com.gome.ecmall.homepage.activity.GomePlusHomeActivity", 30)

driver.quit()
