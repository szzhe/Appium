import os

from time import sleep
from appium import webdriver

from aibizhi import swipe

apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '4.4.2'  # 设备系统版本
desired_caps['deviceName'] = '127.0.0.1:66021'  # 设备名称

# 测试apk包的路径
desired_caps['app'] = apk_path + '\\aibizhi.apk'
# desired_caps['app'] = "E:\\aibizhi.apk"

# 不需要每次都安装apk
desired_caps['noReset'] = True

# 应用程序的包名 aapt dump badging xx.apk
desired_caps['appPackage'] = 'com.lovebizhi.wallpaper'
desired_caps['appActivity'] = 'com.adesk.picasso.view.MainActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app

driver.wait_activity("com.adesk.picasso.view.HomeActivity", 30)
# current_activity = driver.current_activity
# print(current_activity)

# contexts = driver.contexts
# print(contexts) # ['NATIVE_APP']

category = driver.find_elements_by_id("com.lovebizhi.wallpaper:id/thumb")[3].click()
sleep(2)

categorys = driver.find_elements_by_id("com.lovebizhi.wallpaper:id/thumb")[8].click()
sleep(2)

driver.find_element_by_id("com.lovebizhi.wallpaper:id/bp_head_detail_img_loading").click()

swipe.swipLeft(driver, 3)
sleep(2)
swipe.swipRight(driver, 3)
sleep(2)

driver.quit()
