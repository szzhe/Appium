import os
from appium import webdriver
from time import sleep

from Gome import swipe, Captcha, Vecode
from PIL import Image,ImageEnhance

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
desired_caps['noReset'] = False

# 应用程序的包名 aapt dump badging xx.apk
desired_caps['appPackage'] = 'com.gome.eshopnew'
desired_caps['appActivity'] = 'com.gome.ecmall.home.LaunchActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app

# 引导组图
sleep(8)

for i in range(4):
    swipe.swipLeft(driver)
    sleep(2)

driver.wait_activity("com.gome.ecmall.homepage.activity.GomePlusHomeActivity", 30)

# 关闭主页弹窗
# driver.find_element_by_id("com.gome.eshopnew:id/btn_main_adv_close").click()
# sleep(2)

# 进入我的 - 登录账号
driver.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")[4].click()

driver.find_element_by_id("com.gome.eshopnew:id/login_username_edit").clear()
driver.find_element_by_id("com.gome.eshopnew:id/login_username_edit").send_keys("15810795067")
# 国美安全键盘
driver.find_element_by_id("com.gome.eshopnew:id/login_password_edit").click()
driver.find_element_by_id("com.gome.eshopnew:id/bangclepay_keyboard_button_s").click()
driver.find_element_by_id("com.gome.eshopnew:id/bangclepay_keyboard_button_z").click()
driver.find_element_by_id("com.gome.eshopnew:id/bangclepay_keyboard_button_z").click()
driver.find_element_by_id("com.gome.eshopnew:id/bangclepay_keyboard_button_h").click()
driver.find_element_by_id("com.gome.eshopnew:id/bangclepay_keyboard_button_e").click()
driver.find_element_by_id("com.gome.eshopnew:id/bangclepay_keyboard_button_letter_num_shift").click()
driver.find_element_by_id("com.gome.eshopnew:id/bangclepay_keyboard_button_t").click()
driver.find_element_by_id("com.gome.eshopnew:id/bangclepay_keyboard_button_p").click()
driver.find_element_by_id("com.gome.eshopnew:id/bangclepay_keyboard_button_y").click()
driver.find_element_by_id("com.gome.eshopnew:id/bangclepay_keyboard_button_u").click()
driver.find_element_by_id("com.gome.eshopnew:id/bangclepay_keyboard_letter_button_ok").click()
driver.find_element_by_id("com.gome.eshopnew:id/login_button").click()
sleep(2)

pic_path = Captcha.identifyingCode(driver, 525, 391, 645, 439)  # F:\PycharmProjects\Appium\Gome675
pic = pic_path + '\\' + os.listdir(pic_path)[2]
# print("pic:",pic) # F:\PycharmProjects\Appium\Gome\Image
pic_open = Image.open(pic)
print("pic_open:",pic_open)
enhancer = ImageEnhance.Contrast(pic_open)
pic_open = im = enhancer.enhance(2)
vcode = Captcha.convert(pic_path, pic_open)
print("vcode is :", vcode)

# image = Image.open(os.getcwd() + '\\indent_enhance.png').convert("L")
# Vecode.twoValue(image, 140)
# Vecode.clearNoise(image, 4, 4)
# Vecode.saveImage("F:/PycharmProjects/Appium/Gome/5.jpg", image.size)

driver.quit()
